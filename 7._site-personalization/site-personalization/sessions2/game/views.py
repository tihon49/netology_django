from django.shortcuts import render
import random
from .models import Player, Game
from .forms import NumForm


def show_home(request):
    context = {}
    template = 'home.html'

    user_id = request.session.session_key
    if not user_id:
        request.session.cycle_key()
        user_id = request.session.session_key

    player = Player.objects.filter(s_id=user_id).first()
    if not player:
        player = Player.objects.create(s_id=user_id)

    games = Game.objects.filter(is_finished=False)
    done_games = Game.objects.filter(is_active=False, is_finished=False)

    if done_games:
        print('мы в done_games')
        game = done_games.first()
        context['try_count'] = game.try_count
        context['true_num'] = game.num
        if player == game.master:
            context['master'] = True
        game.is_finished = True
        game.save()
    else:
        if not games:
            print('создаем новую игру')
            random_num = random.randint(1, 100)
            game = Game.objects.create(master=player, num=random_num)
            game.save()
            context['random_num'] = random_num
        else:
            print('берем текущую игру')
            game = games.first()
            game.save()

            if player == game.master:
                print('играем за мастера')
                context['random_num'] = game.num
            elif player != game.master:
                print('играем за второго игрока')
                game.players.add(player)
                game.save()
                form = NumForm(request.POST)
                context['form'] = form
                if form.is_valid():
                    guess_num = int(request.POST['num'])
                    game.try_count += 1
                    true_num = game.num

                    if guess_num > true_num:
                        context['message'] = f'{guess_num} больше чем загаданное число'
                    elif guess_num < true_num:
                        context['message'] = f'{guess_num} меньше чем загаданное число'
                    elif guess_num == true_num:
                        context['message'] = f'{guess_num} равно {true_num}!!!'
                        game.is_active = False
                    game.save()

    return render(request, template, context)
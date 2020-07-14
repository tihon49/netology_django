from pprint import pprint

from django.shortcuts import render
import random
from .models import Player, Game
from .forms import MyIntForm, OwnerForm


def show_home(request):
    data = dict()

    user_id = request.session.session_key

    if not user_id:
        request.session.cycle_key()
        user_id = request.session.session_key

    # берем нового игрока, и если его нет - создаем
    player = Player.objects.filter(s_id=user_id).first()
    if not player:
        player = Player.objects.create(s_id=user_id)

    games = Game.objects.filter(is_finished=False)
    done_games = games.filter(is_active=False)
    if done_games:
        game = done_games.first()
        data['try_count'] = game.try_count
        game.is_finished = True
        game.save()
    else:
        if not games:
            rand_num = random.randint(0, 100)
            game = Game.objects.create(owner=player, num=rand_num)
            game.players.add(player)
            data['random_num'] = game.num
        else:
            game = games.first()
            if game.owner != player:
                game.players.add(player)
                data['form'] = MyIntForm()
            else:
                data['random_num'] = game.num

    if request.method == 'POST':
        num = int(request.POST.get('owner_text'))
        print(num)
        true_num = int(game.num)

        if num > true_num:
            data['tip'] = "Вы ввели слишком большое число!"
            game.try_count += 1
            game.save()
        elif num < true_num:
            game.try_count += 1
            game.save()
            data['tip'] = "Вы ввели слишком маленькое число!"
        elif num == true_num:
            game.try_count += 1
            data['tip'] = "Успех"
            game.is_active = False
            game.save()

    return render(
        request,
        'home.html',
        context=data
    )

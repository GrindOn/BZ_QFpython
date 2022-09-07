def can_play(clock):
    print('最外层函数被调用了,clock = {}'.format(clock))

    def handle_action(fn):
        print('handle_action被调用了')

        def do_action(name, game):
            if clock < 21:
                fn(name, game)
            else:
                print('太晚了，不能玩儿游戏了')

        return do_action

    return handle_action


@can_play(12)
def play_game(name, game):
    print(name + '正在玩儿' + game)


play_game('张三', '王者荣耀')

def about_user():
    user_information = {
        "Ваше имя:": str,
        "Ваша фамилия:": str,
        "Ваш год рождения:": int,
        "Город в котором проживаете:": str,
        "Ваш email:": str,
        "Номер телефона:": int,
    }
    about = {}
    for information, user_input in user_information.items():
        user_answers = input(f"Заполните поле: '{information}'  ")
        about[information] = user_input(user_answers)
    print(about)
    about = about_user()
about_user()

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

# Create your views here.

all_items = [
	{'id': 1, 'title': 'Aurora 11-024 Аврора Медведь 30 см', 'price': 527, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет', 'более 12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['soft_toys'], 'describe': 'Игрушка изготовлена из экологически чистых материалов: высококачественного плюшa и гипoaллepгeнного cинтепoна. Не деформируется и не теряет внешний вид при машинной стирке.', 'more': 'Бренд : Aurora. Артикул : 11-024. Размер упаковки: 0.01 х 0.01 х 0.01 м. Вес : 0.01 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/bd0/873_540_10240811ca8906714d1a9f41f2f5b358d/1f753ea1_7425_11e2_8fb8_002655824cb4.jpeg'},
	{'id': 2, 'title': 'Aurora 615-59 Аврора Медведь коричневый', 'price': 759, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет', 'более 12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['soft_toys'], 'describe': 'Большой мишка, не выцветает и не деформируется при стирке.', 'more': 'Бренд : Aurora. Артикул : 615-59. Размер упаковки: 0.34 х 0.14 х 0.2 м. Вес : 0.42 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/3b4/500_500_10240811ca8906714d1a9f41f2f5b358d/4ab930ac_a5a0_11e2_967d_002655824cb6.jpeg'},
	{'id': 3, 'title': 'Aurora 110-07 Аврора Медведь 80 см', 'price': 4349, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет', 'более 12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['soft_toys'], 'describe': 'Мягкая игрушка изготовлена из высококачественных материалов, не деформируется и не выцветает при стирке.', 'more': 'Бренд : Aurora. Артикул : 110-07. Размер упаковки: 0.8 х 0.28 х 0.34 м. Вес : 2.24 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/880/500_500_10240811ca8906714d1a9f41f2f5b358d/60cf2351_bc5b_11e2_968a_002655824cb6.jpeg'},
	{'id': 4, 'title': 'Aurora 21-137 Аврора Медведь медовый, 45 см', 'price': 1399, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет', 'более 12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['soft_toys'], 'describe': 'Классический медведь медового цвета. Игрушка изготовлена из экологически чистых материалов: высококачественного плюшa и гипoaллepгeнного cинтепoна. Не деформируется и не теряет внешний вид при машинной стирке.', 'more': 'Бренд : Aurora. Артикул : 21-137. Размер упаковки: 0.17 х 0.24 х 0.45 м. Вес : 0.45 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/370/500_500_10240811ca8906714d1a9f41f2f5b358d/73e001d5_e5b0_11df_9723_00210091c2bb.jpeg'},
	{'id': 5, 'title': 'Aurora 11-415 Аврора Медведь, 80 см', 'price': 3999, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет', 'более 12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['soft_toys'], 'describe': 'Игрушка изготовлена из экологически чистых материалов: высококачественного плюшa и гипoaллepгeнного cинтепoна. Не деформируется и не теряет внешний вид при машинной стирке.', 'more': 'Бренд : Aurora. Артикул : 11-415. Размер упаковки: 0.3 х 0.44 х 0.8 м. Вес : 2.47 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/d2d/500_500_10240811ca8906714d1a9f41f2f5b358d/635459f5_5e2b_11e2_8fb8_002655824cb6.jpeg'},
	{'id': 6, 'title': 'Aurora 21-237 Аврора Медведь коричневый, 45 см', 'price': 1399, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет', 'более 12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['soft_toys'], 'describe': 'Классический медведь коричневого цвета. Игрушка изготовлена из экологически чистых материалов: высококачественного плюшa и гипoaллepгeнного cинтепoна. Не деформируется и не теряет внешний вид при машинной стирке.', 'more': 'Бренд : Aurora. Артикул : 21-237. Размер упаковки: 0.17 х 0.24 х 0.45 м. Вес : 0.475 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/4fa/500_500_10240811ca8906714d1a9f41f2f5b358d/73e001db_e5b0_11df_9723_00210091c2bb.jpeg'},
	{'id': 7, 'title': 'Aurora 1155 Аврора Медведь, 43 см', 'price': 1999, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет', 'более 12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['soft_toys'], 'describe': 'Игрушка изготовлена из экологически чистых материалов: высококачественного плюшa и гипoaллepгeнного cинтепoна. Не деформируется и не теряет внешний вид при машинной стирке.', 'more': 'Бренд : Aurora. Артикул : 1155. Размер упаковки: 0.2 х 0.26 х 0.43 м. Вес : 0.671 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/ce9/500_500_10240811ca8906714d1a9f41f2f5b358d/73e001c9_e5b0_11df_9723_00210091c2bb.jpeg'},
	{'id': 8, 'title': 'Aurora 21-611 Аврора Медведь белый сидячий, 74', 'price':  2349, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет', 'более 12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['soft_toys'], 'describe': 'Игрушка изготовлена из экологически чистых материалов: высококачественного плюшa и гипoaллepгeнного cинтепoна. Не деформируется и не теряет внешний вид при машинной стирке.', 'more': 'Бренд : Aurora. Артикул : 21-611. Размер упаковки: 0.74 х 0.26 х 0.35 м. Вес : 1.62 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/4ae/873_540_10240811ca8906714d1a9f41f2f5b358d/e54faf62_6b67_11e2_8fb8_002655824cb4.jpeg'},
	{'id': 9, 'title': 'Aurora 30-349 Аврора Медведь коричневый 69 см', 'price': 2949, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет', 'более 12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['soft_toys'], 'describe': 'Классический медведь коричневого цвета. Игрушка изготовлена из экологически чистых материалов: высококачественного плюшa и гипoaллepгeнного cинтепoна. Не деформируется и не теряет внешний вид при машинной стирке.', 'more': 'Бренд : Aurora. Артикул : 30-349. Размер упаковки: 0.5 х 0.38 х 0.26 м. Вес : 1.16 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/f8b/500_500_10240811ca8906714d1a9f41f2f5b358d/7690bcdf_74f7_11e2_8fb8_002655824cb4.jpeg'},
	{'id': 10, 'title': 'PLAY-DOH 37366 Набор "Мистер Зубастик" Новая Версия', 'price': 1239, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['games'], 'describe': 'Не секрет, что многие дети, а порой даже и взрослые, относятся к посещению стоматолога с большой опаской. С помощью этого своеобразного и очень интересного игрового набора ребёнок сможет не только проявить свои творческие способности и скульптурные таланты, занимаясь лепкой из пластилиновой массы, но и в простой увлекательной игровой форме познакомиться с основными принципами работы зубного врача, а также понять важность регулярного и правильного ухода за зубками.', 'more': 'Бренд : PLAY-DOH. Артикул : 37366. Размер упаковки: 0.087 х 0.257 х 0.229 м. Вес : 0.84 кг', 'img': 'http://www.toy.ru/upload/iblock/3a2/4bec74ac_6131_11e5_a105_00155d093116.jpeg'},
	{'id': 11, 'title': 'Сквуши Набор для творчества "Мороженое" - масса для лепки и аксессуары', 'price': 1219, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['games'], 'describe': 'Вкусное, сладкое, ароматное…Ммм…Мороженое! Теперь его можно сделать самостоятельно и украсить на свой вкус. С набором для творчества Сквуши Ваш ребенок создаст множество разнообразных десертов и лакомств. Можно создавать классические молочные шарики с разными вкусами или заняться изготовлением фруктового льда. Эскимо или замороженные пирожные? Количество вариантов не ограничено! Яркие цвета и приятный состав Сквуши сделают игру очень увлекательной и интересной.', 'more': 'Бренд : Skwooshi. Артикул : S30024. Размер упаковки: 0.23 х 0.09 х 0.23 м. Вес : 0.542 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/1f6/873_540_10240811ca8906714d1a9f41f2f5b358d/daca31e4_be9e_11e5_84ee_00155d093116.jpeg'},
	{'id': 12, 'title': 'PLAY-DOH B0307 Игровой набор "Магазинчик печенья"', 'price': 629, 'ages': ['1-3 года', '4-5 лет', '6-8 лет', '9-12 лет'], 'sex': ['для мальчиков', 'для девочек'], 'category': ['games'], 'describe': 'Яркий и занимательный игровой набор PLAY-DOH (Плэй-До) для ребенка, стремящегося к творчеству и проявляющего желание попробовать себя в художественной лепке из пластилина.. . Комплект состоит из пяти стандартных контейнеров с массой для лепки, а также большое количество различных аксессуаров для «выпекания» аппетитных кондитерских шедевров. В упаковке Вы найдете – миниатюрную скалку для раскатывания «теста», игрушечный противень для выпечки, различные формы для лепки фигурного печенья, кухонная лопатка, а также специальный инструмент, с помощью которого ребенок сможет украшать готовые изделия так, как подскажет ему фантазия.', 'more': 'Бренд : PLAY-DOH. Артикул : B0307. Размер упаковки: 0.23 х 0.07 х 0.23 м. Вес : 0.625 кг', 'img': 'http://m.toy.ru/upload/resize_cache/iblock/22b/873_540_10240811ca8906714d1a9f41f2f5b358d/6db103b0_6130_11e5_a105_00155d093116.jpeg'},
]

def add(request):
    return HttpResponse("Добавлено")

def home(request):
    """
    Home page with auth links.
    """
    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")

@login_required
def account_profile(request):
    """
    Show user greetings. ONly for logged in users.
    """
    return HttpResponse("Hi, {0}! Nice to meet you.".format(request.user.first_name))


def account_logout(request):
    """
    Logout and redirect to the main page.
    """
    logout(request)
    return redirect('/') 

def start(request):
    return render(request, "index.html")

def catalog(request):
    return render(request, "catalogue.html")

def soft_toys(request):
	items_list_st = []
	for i in range(len(all_items)):
		info = all_items[i]
		categories = info['category']
		cat = False
		for j in range(len(categories)):
			if categories[j] == 'soft_toys':
				cat = True
		if cat:
			items_list_st.append(info)	
	return render(request, "soft_toys.html", {'items_list': items_list_st})

def games(request):
	items_list_gh = []
	for i in range(len(all_items)):
		info = all_items[i]
		categories = info['category']
		cat = False
		for j in range(len(categories)):
			if categories[j] == 'games':
				cat = True
		if cat:
			items_list_gh.append(info)
	return render(request, "games.html", {'items_list': items_list_gh})

def cart(request):
	return render(request, "cart.html")

def toy1(request):
	item = all_items[0]
	return render(request, "toy.html", {'item': item})

def toy2(request):
	item = all_items[1]
	return render(request, "toy.html", {'item': item})

def toy3(request):
	item = all_items[2]
	return render(request, "toy.html", {'item': item})

def toy4(request):
	item = all_items[3]
	return render(request, "toy.html", {'item': item})

def toy5(request):
	item = all_items[4]
	return render(request, "toy.html", {'item': item})

def toy6(request):
	item = all_items[5]
	return render(request, "toy.html", {'item': item})

def toy7(request):
	item = all_items[6]
	return render(request, "toy.html", {'item': item})

def toy8(request):
	item = all_items[7]
	return render(request, "toy.html", {'item': item})

def toy9(request):
	item = all_items[8]
	return render(request, "toy.html", {'item': item})

def toy10(request):
	item = all_items[9]
	return render(request, "toy.html", {'item': item})

def toy11(request):
	item = all_items[10]
	return render(request, "toy.html", {'item': item})

def toy12(request):
	item = all_items[11]
	return render(request, "toy.html", {'item': item})
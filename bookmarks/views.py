from django.shortcuts import render, redirect
from product.models import Product
from django.http import JsonResponse


def bookmarks(request):
    liked_items = request.session.get('bookmarks')
    bookmarks_list = list()
    print('liked: ', liked_items)
    if liked_items:
        for i in liked_items:
            try:
                liked = Product.objects.filter(id=int(i), in_stock=True)
                if liked:
                    bookmarks_list.append(liked[0])

                # bookmarks_list.append(Product.objects.get(id=int(i)))
            except Exception as ex:
                print(ex, 'No product with ID {} in DB'.format(i))
                request.session['bookmarks'].remove(i)
                request.session.modified = True
        print(bookmarks_list)
    return render(request, 'bookmarks/bookmarks.html', {'bookmarks': bookmarks_list})


def add_to_bookmarks(request):
    print('we are here')
    if request.method == 'POST':
        print('adding', request.POST)
        if not request.session.get('bookmarks'):
            request.session['bookmarks'] = list()
        else:
            request.session['bookmarks'] = list(request.session['bookmarks'])

        # chek if item exists
        item_exists = next((item for item in request.session['bookmarks'] if item == request.POST.get('id')), False)

        if not item_exists:
            request.session['bookmarks'].append(request.POST.get('id'))
            request.session.modified = True
    if request.is_ajax:
        data = {'id': request.POST.get('id')}
        print('ajax')
        print('request: ', request)
        request.session.modified = True
        return JsonResponse(data)

    return redirect(request.POST.get('url_from'))


def remove_from_bookmarks(request):
    print('we got removeRequest')
    if request.method == 'POST':
        request.session['bookmarks'].remove(request.POST.get('id'))
        request.session.modified = True

    if request.is_ajax:
        counter = len(request.session['bookmarks'])
        request.session.modified = True
        data = {'id': request.POST.get('id'), 'counter': counter}
        return JsonResponse(data)

    return redirect(request.POST.get('url_from'))


def remove_bookmarks(request):
    if request.session.get('bookmarks'):
        del request.session['bookmarks']
        request.session.modified = True
        return redirect(request.POST.get('url_from'))


def bookmarks_api(request):
    return JsonResponse(request.session.get('bookmarks'), safe=False)

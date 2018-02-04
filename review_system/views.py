# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Reviews
from models import Map

# Create your views here.


def home(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


def user_inputs(request):
    template_name = 'user_inputs.html'
    context = {}
    return render(request, template_name, context)


def dashboard(request):
    template_name = 'dashboard.html'
    reviews = Reviews.objects.all()
    ratings_and_reviews = []
    for obj in reviews:
        rating_and_review = [obj.rating, obj.review]
        ratings_and_reviews.append(rating_and_review)
    context = {'ratings_and_reviews': ratings_and_reviews}
    return render(request, template_name, context)


def place(request):
    place_id = 'ChIJBX5nLYjeKDoRjsQTS6jzeho'
    template_name = 'place.html'
    context = {}
    review_query = Map.objects.get(place_id=place_id)
    context['rating'] = review_query.rating
    context['review'] = review_query.review
    context['address'] = review_query.address
    return render(request, template_name, context)

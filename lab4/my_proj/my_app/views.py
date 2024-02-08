from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

def title_name(string1: str):
    return string1.lower()



class HomePageView(View):
    def get(self, request):

        my_name = "harRy"
        new_name = title_name(my_name)
        
        names_list = ["HARRY", "DILLON"]

        names_list.append("TanK")
        

        new_names = my_functions.title_names(names_list)

        car1 = my_objects.Car("purple", "VROOM")
        car2 = my_objects.Car("orange", "crash")






        my_context = {'hi':'hello world!',
                      'name':new_name,
                      'new_names':new_names,
                      'car1': car1,
                      'car2': car2




                      }


     
        return render(request, 'my_app/index.html',my_context)
    





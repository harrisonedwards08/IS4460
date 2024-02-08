from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

def title_name(string1: str):
    return string1.title()



class HomePageView(View):
    def get(self, request):

        my_name = "harRy"
        new_name = title_name(my_name)
        
        names_list = ["HARRY", "DILLON"]

        names_list.append("TanK")
        

        new_names = my_functions.title_names(names_list)

        car1 = my_objects.Car("purple", "Vroom")
        car2 = my_objects.Car("orange", "Crash")
        bike1 = my_objects.motorcycle("black","BRAAP BRAAP")






        my_context = {'hi':'hello world!',
                      'oldname': my_name,
                      'new_name':new_name,
                      'old_names': names_list,
                      'new_names':new_names,
                      'car1': car1,
                      'car2': car2,
                      'bike1': bike1




                      }


     
        return render(request, 'my_app/index.html',my_context)
    





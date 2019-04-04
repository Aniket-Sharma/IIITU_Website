from django.views.generic import TemplateView
from django.conf import settings

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

#
# class ChangeLanguageView(TemplateView):
#     template_name = 'main/change_language.html'


class HomePageView(TemplateView):
    template_name = 'main/home.html'



class PlacementDeskView(TemplateView):
    template_name = 'main/PlacementDesk.html'
    def get_logos(self):
        image_list = []
        image_folder = settings.STATICFILES_DIRS
        for file in image_folder:
            if file.endswith(".png"):
                image_list.append(file)
        return render(request, 'main/placementDesk.html', {'brands': image_list})


class ReachView(TemplateView):
    template_name = 'main/Reach.html'




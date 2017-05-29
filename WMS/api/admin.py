from django.contrib import admin
from .models import Reading


class ReadingModelAdmin(admin.ModelAdmin):
    ''' You're giving the order in which the fields are to be present
        The column title will be captalized.
        To change the title of the column(owner->updated_by), so that it reflects a particular field(eg: owner)
         in the model, do the following
    '''
    list_display = ['id', 'Updated_By', 'temperature', 'pressure', 'humidity', 'updated']

    def Updated_By(self, instance):
        return instance.owner


    class Meta:
        model = Reading
        ordering = ['-id']



admin.site.register(Reading, ReadingModelAdmin)

from django import forms
from django.contrib import admin
from nucleo.models import User,Category,Project,Participate

class UserAdminForm(forms.ModelForm):
    def clean_name(self):
        if len(self.cleaned_data['name'])<3:
            raise forms.ValidationError('El nombre es demasiado corto')
        
        elif len(self.cleaned_data['name'])>24:
                raise forms.ValidationError('El nombre es demasiado largo')
        else:
            return self.cleaned_data['name']
        
    def clean_surname(self):
        if len(self.cleaned_data['surname'])<3:
            raise forms.ValidationError('El apellido es demasiado corto')
        
        elif len(self.cleaned_data['surname'])>24:
                raise forms.ValidationError('El apellido es demasiado largo')
        else:
            return self.cleaned_data['surname']   
      
class ProjectAdminForm(forms.ModelForm):
    def clean_title(self):
        if len(self.cleaned_data['title'])<3:
            raise forms.ValidationError('El titulo es demasiado corto')
        
        elif len(self.cleaned_data['title'])>52:
                raise forms.ValidationError('El titulo es demasiado largo')
        else:
            return self.cleaned_data['title']
        
    def clean_level(self):
        if (self.cleaned_data['level'])<1:
            raise forms.ValidationError('El nivel no puede ser inferior a 1')
        
        elif (self.cleaned_data['level'])>10:
                raise forms.ValidationError('El nivel máximo es 10')
        else:
            return self.cleaned_data['level']     
        
class ProjectInLine(admin.StackedInline):
    model=Project
    max_num=3
    

class CategoryAdmin(admin.ModelAdmin):
    list_filter=['id','name']
    ordering=['name']
    list_per_page=5 
    inlines=[ProjectInLine,]

class ProjectAdmin(admin.ModelAdmin):
    form=ProjectAdminForm
    list_filter=['title']
    ordering=['title']
    list_per_page=5 
    list_display = ('id','title', 'level', 'startDate', 'endDate', 'idCategory',)
    search_fields= ('title','idCategory')    

class UserAdmin(admin.ModelAdmin):
    form=UserAdminForm
    list_filter=['role_user']
    ordering=['name']
    list_per_page=5 
    list_display = ('username','name', 'surname', 'address', 'role_user',)
    search_fields= ('name','surname')
    
    
class ParticipateAdmin(admin.ModelAdmin):
    list_filter=['idCliente']
    ordering=['id']
    list_per_page=5 
    list_display = ('id', 'idCliente','idProject')



admin.site.register(User,UserAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Participate,ParticipateAdmin)

from django import forms

class FormCorreo(forms.Form):
    nombre = forms.CharField(label="Tu Nombre",
                             widget=forms.TextInput(attrs={"placeholder": "Tu Nombre", 
                                                           "class": "form-control"}),
                             max_length=100
                             )
    
    email = forms.CharField(label="Tu Correo Electrónico",
                            widget=forms.TextInput(attrs={"placeholder": "Tu Correo Electrónico", 
                                                          "class": "form-control"})
                            )
    
    asunto = forms.CharField(label="Asunto",
                             widget=forms.TextInput(attrs={"placeholder": "Asunto",
                                                           "class": "form-control"}),
                             max_length=100
                             )
    
    mensaje = forms.CharField(label="Mensaje",
                              widget=forms.Textarea(attrs={"placeholder": "Mensaje",
                                                           "class": "form-control"})
                              )
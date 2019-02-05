from django.forms import ModelForm

from .models import FamilyMember, Profile
from django.forms import inlineformset_factory

from .models import Revenda
from veiculo.models import Veiculo



class FamilyMemberForm(ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()

FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember, form=FamilyMemberForm, extra=1)




class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        exclude = ()

RevendaFormSet = inlineformset_factory(Revenda, Veiculo, form=VeiculoForm, extra=1)


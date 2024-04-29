from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not nome_válido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome deve ser válido'})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de CPF inválido'})        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O rg deve ter 9 dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O celular deve seguir este modelo (XX) 9 XXXX-XXXX. (respeitando os espaços e traços)'})

        return data
        
        
        
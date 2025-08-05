#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class TestApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Título do app
        title = Label(
            text='Meu Primeiro App Android em Python!',
            size_hint=(1, 0.2),
            font_size='20sp',
            halign='center'
        )
        
        # Campo de entrada de texto
        self.text_input = TextInput(
            hint_text='Digite algo aqui...',
            size_hint=(1, 0.2),
            multiline=False
        )
        
        # Botão de ação
        button = Button(
            text='Clique Aqui!',
            size_hint=(1, 0.2),
            font_size='18sp'
        )
        button.bind(on_press=self.on_button_click)
        
        # Label para mostrar resultado
        self.result_label = Label(
            text='Resultado aparecerá aqui',
            size_hint=(1, 0.4),
            font_size='16sp',
            halign='center'
        )
        
        # Adicionar widgets ao layout
        layout.add_widget(title)
        layout.add_widget(self.text_input)
        layout.add_widget(button)
        layout.add_widget(self.result_label)
        
        return layout
    
    def on_button_click(self, instance):
        texto = self.text_input.text
        if texto:
            self.result_label.text = f'Você digitou: "{texto}"'
        else:
            self.result_label.text = 'Digite algo no campo acima!'


if __name__ == '__main__':
    TestApp().run()

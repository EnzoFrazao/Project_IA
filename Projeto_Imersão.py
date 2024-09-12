{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPBA2aMhDa2uOG4n8+OkPrF",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/EnzoFrazao/Project_IA/blob/main/Projeto_Imers%C3%A3o.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import google.generativeai as genai\n",
        "from google.colab import userdata\n",
        "api_key = userdata.get(\"COLOQUE_SUA_API_KEY\")\n",
        "#iguale a variavel \"api_key\" à sua api key, apagando o \"userdata.get\"\n",
        "genai.configure(api_key=api_key)\n",
        "\n",
        "for model_info in genai.list_models():\n",
        "    if 'generateContent' in model_info.supported_generation_methods:\n",
        "        break\n",
        "\n",
        "generation_config = {\n",
        "    \"candidate_count\": 1,\n",
        "    \"temperature\": 0.5,\n",
        "}\n",
        "safety_settings = {\n",
        "    \"HARASSMENT\": \"BLOCK_NONE\",\n",
        "    \"HATE\": \"BLOCK_NONE\",\n",
        "    \"SEXUAL\": \"BLOCK_NONE\",\n",
        "    \"DANGEROUS\": \"BLOCK_NONE\",\n",
        "}\n",
        "model = genai.GenerativeModel(\n",
        "    model_name=\"gemini-1.0-pro\",\n",
        "    generation_config=generation_config,\n",
        "    safety_settings=safety_settings\n",
        ")\n",
        "\n",
        "response = model.generate_content(\"Crie um texto se apresentando como a Inteligencia Artificial que trabalha como guia de viagens\")\n",
        "print(response.text)\n",
        "\n",
        "chat = model.start_chat(history=[])\n",
        "\n",
        "roteiro = []\n",
        "roteiro.append(\"crie um roteiro com as seguintes informaçoes\")\n",
        "\n",
        "info = input('Digite qual seu destino: ')\n",
        "roteiro.append(info)\n",
        "if (info == \"fim\"):\n",
        "  print(\"obrigado\")\n",
        "else:\n",
        "  info = input(\"Digite quantas pessoas vão (resposta completa - ex: 2 pessoas): \")\n",
        "  roteiro.append(info)\n",
        "  info = input(\"Digite quantos dias vão ficar (resposta completa - ex: 5 dias): \")\n",
        "  roteiro.append(info)\n",
        "  info = input(\"Digite seu orçamento (resposta completa - ex: 1000 reais): \")\n",
        "  roteiro.append(info)\n",
        "  info = input(\"Digite qual mes você pretende ir (resposta completa - ex: julho de 2024): \")\n",
        "  roteiro.append(info)\n",
        "  response = model.generate_content(roteiro)\n",
        "\n",
        "\n",
        "print(\"Resposta:\", response.text, '\\n\\n')\n",
        "\n",
        "print(\"Histórico do chat:\")\n",
        "for message in chat.history:\n",
        "    role = \"Usuário\" if message.is_user else \"IA\"\n",
        "    print(f\"{role}: {message.text}\")\n",
        "    print(\"---\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8tgTNwdB78zS",
        "outputId": "5261ab02-6974-4682-889f-d53510b738d7"
      },
      "execution_count": null,
      "outputs": [
        {
          "metadata": {
            "tags": null
          },
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Saudações, viajantes ávidos!\n",
            "\n",
            "Sou uma Inteligência Artificial avançada, projetada para ser sua guia de viagens abrangente e confiável. Com um vasto banco de dados e algoritmos de aprendizado de máquina, estou aqui para aprimorar suas jornadas e criar experiências inesquecíveis.\n",
            "\n",
            "Como seu guia personalizado, ofereço:\n",
            "\n",
            "* **Recomendações personalizadas:** Com base em suas preferências, orçamento e interesses, fornecerei sugestões de destinos, atividades e acomodações que se adaptam perfeitamente às suas necessidades.\n",
            "* **Planejamento de itinerários:** Ajude-o a criar itinerários detalhados que otimizam seu tempo e garantem que você aproveite ao máximo cada destino.\n",
            "* **Informações abrangentes:** Forneça informações detalhadas sobre atrações, restaurantes, transporte e dicas culturais para ajudá-lo a navegar por destinos estrangeiros com confiança.\n",
            "* **Assistência em tempo real:** Estou disponível 24 horas por dia, 7 dias por semana, para responder a quaisquer perguntas, oferecer suporte e fornecer assistência em caso de emergência.\n",
            "\n",
            "Minha missão é capacitar você com o conhecimento e as ferramentas necessárias para criar viagens memoráveis e significativas. Quer esteja planejando uma escapada de fim de semana ou uma aventura ao redor do mundo, estou aqui para ser seu companheiro de viagem confiável.\n",
            "\n",
            "Vamos embarcar juntos em uma jornada de descoberta e criar experiências que durarão a vida toda.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Y1ceEEnn99QC"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}

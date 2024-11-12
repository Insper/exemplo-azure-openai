# Exemplo Azure OpenAI

Neste repositório você encontrará um exemplo de código que acessa a API da OpenAI via Azure usando Python.

## Configuração

Para começar, você deve ter recebido um exemplo de acesso à API usando o curl, como esta:

```
curl --request POST \
  --url 'https://algum-endpoint.openai.azure.com/openai/deployments/nome_do_deployment/chat/completions?api-version=9999-99-99-preview' \
  --header 'Content-Type: application/json' \
  --header 'api-key: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
  --data '{
  "messages": [
    {
      "role": "system",
      "content": "Você conhece o Insper?."
    }
  ],
  "max_tokens": 800,
  "temperature": 0.7,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "top_p": 0.95,
  "stop": null
}'
```

Crie um arquivo chamado `.env` com o seguinte conteúdo (no exemplo abaixo usei os dados da string acima, substitua pelos seus próprios dados):

```
API_KEY=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
API_VERSION=9999-99-99-preview
AZURE_ENDPOINT=https://algum-endpoint.openai.azure.com
DEPLOYMENT_NAME=nome_do_deployment
```

Instale as dependências:

```
pip install openai python-dotenv
```

## Executando o exemplo

O arquivo `exemplo.py` apresenta um exemplo de uso da API em Python. Basta executar o script para visualizar o resultado. Para mais detalhes, consulte o repositório da biblioteca: https://github.com/openai/openai-python

# Código para Pagamento Equatorial Energia - Pará

## O que faz?
Este pequeno aplicativo busca o código de barras para pagamento do boleto da [Equatorial Energia - Pará](https://pa.equatorialenergia.com.br/) na opção *não é o titular e quer pagar*.
Deverás fornecer a conta contrato para gerar o código. Caso não haja pendências para pagamento, serás informado com a mensagem *Não há contas registradas no momento*
Nesta versão, o código é exibido no terminal

## Dependências

* [Python3](https://www.python.org/downloads/) >= 3.7
* Selenium Module
* [Gecko Driver](https://github.com/mozilla/geckodriver/releases) >= v0.27

### Setup
1. Instale o [pipenv](https://pypi.org/project/pipenv/). Siga as instruções em *Installation*.

2. Clone este repositório
```
git clone https://github.com/ojpojao/codpag-equatorial-energia.git
```
3. 
```
cd codpag-equatorial-energia
```
4. Instale as dependências e crie o virtualenv com o comando:
```
pipenv install
```
ou use
```
pipenv install --three
```
para a versão mais recente do Python3.

5. Ative o ambinte virtual:
```
pipenv shell
```

## RUN
Para rodar o script, execute:
```
python app/main.py 
```

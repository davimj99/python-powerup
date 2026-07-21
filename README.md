# 🤖 Agente de Automação de Tarefas Acadêmicas

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyAutoGUI-Automação-2ECC71?style=for-the-badge" alt="PyAutoGUI">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/OpenPyXL-Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white" alt="OpenPyXL">
</p>

<p align="center">
  <strong>Automatizando processos acadêmicos com rapidez, precisão e segurança.</strong>
</p>

---

## 📖 Sobre o Projeto

O **Agente de Automação de Tarefas Acadêmicas** foi desenvolvido para automatizar atividades repetitivas em sistemas educacionais, reduzindo significativamente o tempo gasto com lançamentos manuais e minimizando erros humanos.

A aplicação utiliza **Python** e **PyAutoGUI** para controlar automaticamente a interface do sistema, realizando a leitura de informações provenientes de planilhas e executando o preenchimento de notas, avaliações e demais dados acadêmicos de forma rápida, precisa e segura.

---

## ✨ Principais Funcionalidades

- 🤖 **Automação de Lançamento de Notas**
  - Preenchimento automático de avaliações e notas em sistemas acadêmicos.

- 📄 **Leitura Inteligente de Planilhas**
  - Importação de dados estruturados utilizando arquivos Excel.

- 🎯 **Mapeamento de Coordenadas**
  - Captura das posições da tela para configurar os pontos de clique do robô.

- 🗄️ **Gerenciamento das Execuções**
  - Organização das tarefas e controle do fluxo de automação.

- 📊 **Registro das Operações**
  - Acompanhamento das execuções realizadas durante a automação.

- 🛡️ **Fail-Safe Integrado**
  - Interrupção imediata da automação em situações inesperadas, garantindo maior segurança durante a execução.

---

## 🏗️ Estrutura do Projeto

```text
📦 projeto
│
├── codigo.py          # Núcleo principal da automação
├── auxiliar.py        # Captura de coordenadas da tela
├── requerimento.py    # Processamento e validação dos dados
│
├── planilhas/         # Arquivos de entrada
├── logs/              # Registros das execuções

```

---

## ⚙️ Tecnologias Utilizadas

- Python
- PyAutoGUI
- OpenPyXL
- Pillow

---

## 🚀 Instalação

Instale todas as dependências do projeto:

```bash
pip install pyautogui mysqlclient openpyxl pillow
```

---

## 🎯 Objetivo

Este projeto foi desenvolvido para:

- reduzir tarefas repetitivas;
- aumentar a produtividade da equipe;
- minimizar erros de digitação;
- automatizar processos acadêmicos;
- garantir maior confiabilidade na inserção de dados.

---

## 🔒 Segurança

O robô utiliza mecanismos de segurança durante sua execução, incluindo:

- Fail-Safe do PyAutoGUI;
- validação dos dados antes da automação;
- controle do fluxo de execução;
- registro das operações realizadas.

---

## 📌 Observações

Por depender da interface gráfica do sistema acadêmico, a automação necessita que:

- a resolução da tela permaneça configurada corretamente;
- as coordenadas estejam previamente mapeadas;
- o sistema permaneça aberto durante toda a execução.

---

<div align="center">

**Desenvolvido com ❤️ utilizando Python e PyAutoGUI.**

</div>

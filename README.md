# TechReview Blog - Guia de Início Rápido

Este é um blog de reviews de tecnologia moderno construído com **Django** e **Tailwind CSS**.

## Como Rodar o Projeto

### 1. Preparar o Ambiente
O projeto já possui um ambiente virtual e dados iniciais.
```bash
# Ativar o ambiente virtual (Windows)
.\venv\Scripts\activate
```

### 2. Rodar o Servidor Django
```bash
python manage.py runserver
```

### 3. Compilar o Tailwind (Opcional - em desenvolvimento)
Se você fizer alterações no visual, rode o watcher em um terminal separado:
```bash
cd theme/static_src
npm run start
```

## Credenciais de Admin
Você pode acessar o painel administrativo em `http://127.0.0.1:8000/admin/`:
- **Usuário:** `admin`
- **Senha:** `admin123`

## Estrutura do Projeto
- `reviews/`: Lógica principal do blog (modelos, views).
- `theme/`: App dedicado ao Tailwind CSS e design system.
- `templates/`: Templates globais e específicos.
- `media/`: Imagens de reviews e produtos.

## Recursos de SEO Implementados
- **JSON-LD**: Schema.org implementado em cada página de review.
- **OpenGraph**: Meta tags prontas para redes sociais.
- **Slugs Amigáveis**: URLs otimizadas para motores de busca.
- **Robots.txt**: Já configurado na raiz.

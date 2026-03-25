Tutorial GIT:
# Manual GitHub – Receita para as Resenhas

Este manual é um guia passo a passo para você trabalhar nas nossas Resenhas!

---

## 1. Criar sua branch pessoal
Crie uma branch só sua:
```bash
git checkout -b aluno-seunome
git push -u origin aluno-seunome
```
⚠️ Trabalhe **sempre nessa branch**. Nunca altere a `master`.

---

## 2. Pegar novas tarefas
Quando sair coisa nova:
```bash
git fetch upstream
git checkout main
git merge upstream/master
git push origin master
```

Sempre houver novas tarefas, elas irão para branch principal. Então é sempre importante fazer esses passos.

---

## 3. Trazer as tarefas para sua branch
```bash
git checkout aluno-seunome
git merge main
```

👉 Se aparecer conflito (`<<<<<<<` e `>>>>>>>`), edite o arquivo, salve e rode:
```bash
git add .
git commit
```

---

## 4. Fazer a Rezenha e entregar

Depois de Resenhar:
```bash
git add .
git commit -m "Tarefa X feita"
git push origin aluno-seunome
```

---

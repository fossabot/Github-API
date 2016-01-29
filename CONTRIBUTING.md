Si cela vous intéresse, cette page est un guide vous permettant d'optimiser votre participation.

## Comment participer ?
Puisque le projet est hébergé sur Github, le moyen le plus simple est de cloner le projet.
Je vous encourage de consulter le [guide officiel](https://help.github.com/articles/fork-a-repo) pour plus d'informations.

Une fois votre développement terminé, il vous suffira alors de [proposer une pull request](https://help.github.com/articles/using-pull-requests).

#### Quoi mettre dans un message commit ?
Après avoir effectuer toutes les modifications, vous utilisez la commande 
```bash
git commit -m "Votre message" 
```
Le message doit indiquer brièvement mais clairement ce qui a été modifier dans le dépôt.

#### Quand créer une branche ?
Vous pouvez créer une branche en utilisant la commande 
```bash
git branch
```
Il est recommandé de créer une branche lorsque vous voulez effectuer plusieurs modifications dans le projet de votre coté sans toucher au projet principale.


#### Comment faire les fusions ?
Quand vous terminez le travail sur une branche, vous pouvez fusionner vos modifications vers la branche master en utilisant la commande 
```bash
git merge
```

## Sur quoi travailler ?
Si vous avez envie de participer, mais que vous ne savez pas sur quoi travailler, vous pouvez consulter la [liste des issues ouvertes](https://github.com/glo2003/team9/issues?state=open).

### Ordre de priorités
Chaque ticket est associé à un ou plusieurs label permettant de les classifier, et donc de déterminer leur importance.

## Si vous trouvez un bug ?
Avant de faire un pull-request, il est important de créer un issue et de bien spécifier les conditions sous-lesquelles le bug s'est produit et les informations relatives à votre configuration.
Assurez-vous de respecter la syntaxe et les normes de programmation suivis dans le projet. Par la suite, vous pourrez faire valider vos modifications.

## Comment mon travail est validé ?
Lorsque vous proposez une pull request, un responsable du projet va contrôler votre travail selon plusieurs aspects :
* Fonctionnellement : la plus value de votre travail est acceptable et aucune régression n'est introduite.
* Qualité de code : le code livré est propre, maintenable, testé.
* Style de code : votre travail est dans la lignée du travail existant, et ne représentera pas une verrue au milieu du reste du projet.

# RATISS-Framework

## Protocole d’audit scientifique exécutable

[![CI](https://github.com/jonathansearch/RATISS-Framework/actions/workflows/tests.yml/badge.svg)](https://github.com/jonathansearch/RATISS-Framework/actions/workflows/tests.yml)
![Tests](docs/badges/tests.svg) ![Dépendances](docs/badges/stdlib.svg) ![Licence](docs/badges/license.svg) ![R7](docs/badges/r7.svg)

> **RATISS-Framework** est la couche de méthode et de contrôle de RATISS Labs. Il fournit un protocole d’audit exécutable en Python standard, fondé sur les hashes scellés, les journaux de déviations chaînés, les bornes de plausibilité physique, la résolution d’identifiants et une commande unique de rejeu des verdicts publiés.

![RATISS Framework](docs/img/logo-ratiss-labs.png)

![Bannière RATISS Framework](docs/img/banniere-framework.png)

---

## 1. Positionnement

RATISS-Framework transforme des exigences d’intégrité scientifique en contrôles exécutables. Le dépôt ne remplace pas l’expertise scientifique et ne déclare pas qu’un résultat est vrai par simple conformité technique. Il vérifie plutôt que les éléments annoncés sont identifiables, scellés, rejouables et correctement documentés.

Le framework constitue la **couche 1** de l’écosystème RATISS Labs. Il juge notamment le dépôt [RATISS-LABS-GTT](https://github.com/jonathansearch/RATISS-LABS-GTT), qui constitue la couche 2 expérimentale. Cette dépendance est scellée et vérifiée en intégration continue.

> **Règle R7 :** aucune affirmation publique sans qu’un tiers puisse la reproduire en une commande.

Le projet utilise exclusivement la bibliothèque standard Python pour son chemin critique. Cette contrainte réduit le nombre de dépendances nécessaires à l’audit et facilite la reproduction dans des environnements contrôlés.

## 2. Résumé exécutif

RATISS-Framework regroupe six fonctions centrales : la vérification d’intégrité par hash, le scellement de manifestes, le journal chaîné des déviations, l’évaluation de bornes de plausibilité physique, la résolution d’identifiants et la génération de rapports d’audit sans sections vides.

Le protocole sépare la construction d’un artefact de son évaluation. L’équipe de création peut produire, modifier et tester les composants. L’équipe Rouge applique ensuite le juge et conserve un droit de veto sur la publication. Un résultat conforme au protocole est donc un résultat documenté, vérifiable et rejouable selon le périmètre annoncé ; il ne constitue pas automatiquement une validation scientifique indépendante.

## 3. Laboratoire et gouvernance

**RATISS Labs** est un laboratoire indépendant basé à Yaoundé, au Cameroun. Le laboratoire audite des artefacts publics de recherche en vérifiant leurs hashes, leurs identifiants, leur plausibilité physique et leur reproductibilité. Chaque rapport est publié avec une annexe de reproduction.

Jonathan Evina est fondateur et chef de laboratoire. Son identifiant ORCID est [0009-0000-4092-5313](https://orcid.org/0009-0000-4092-5313) et son compte GitHub de référence est [jonathansearch](https://github.com/jonathansearch).

Le laboratoire fonctionne avec deux responsabilités distinctes :

| Fonction | Responsabilité | Autorité de publication |
|---|---|---|
| Création | construction, exécution et préparation des artefacts | aucune autorité de publication |
| Équipe Rouge | vérification indépendante, certification ou déclaration de divergence | veto absolu |

L’auditeur conserve la priorité sur le chef de laboratoire lorsqu’un écart est détecté. Cette règle vise à empêcher qu’un impératif de calendrier ou de présentation ne remplace une vérification.

Pour les demandes d’audit, le dépôt public associé est [`ratiss-audit-public`](https://github.com/jonathansearch/ratiss-audit-public). Le contact professionnel est `jonathan.ratisslabs@zohomail.com`.

## 4. La méthode et ses règles

La méthode repose sur une loi opérationnelle unique : un chiffre ou une affirmation publiés doivent être rattachés à un calcul, à des paramètres et à une preuve de reproduction.

| Règle | Énoncé opérationnel |
|---|---|
| **R4** | Le raisonnement conceptuel est toujours autorisé ; un chiffre est publié seulement s’il a été calculé avec ses paramètres et son hash. |
| **R5** | Les prompts et paramètres sont scellés et hashés dans chaque run ; toute modification après mesure devient une déviation journalisée. |
| **R6** | Les bras expérimentaux sont séparés du chemin critique ; le verdict repose sur une ablation avec et sans modification, jamais sur une intuition. |
| **R7** | Aucune affirmation publique n’est publiée sans qu’un tiers puisse la reproduire en une commande. |
| Hérité 1 | Une simulation n’est pas une exécution matérielle. |
| Hérité 2 | Un identifiant enregistré n’est pas une revalidation en temps réel. |

Ces règles sont transcrites dans les modules `verify`, `seal`, `journal`, `bounds`, `ids`, `report` et `__main__`.

## 5. Composants techniques

![Méthode de la loi unique](docs/img/methode-loi-unique.png)

### `verify` — intégrité et formes

Le module `verify` compare un artefact servi à un hash attendu et vérifie les formes nécessaires à l’audit. Il permet d’associer une valeur publiée à des octets effectivement reçus plutôt qu’à une simple adresse ou à une promesse de disponibilité.

### `seal` — manifestes scellés

Le module `seal` construit et vérifie les manifestes. Le scellement rend les paramètres contrôlables avant l’exécution et permet de détecter une modification intervenue après la mesure.

### `journal` — déviations chaînées

Le module `journal` conserve les déviations dans une chaîne vérifiable. Chaque événement s’inscrit dans la continuité du précédent afin que l’ordre et l’intégrité de l’historique puissent être contrôlés.

### `bounds` — plausibilité physique

Le module `bounds` applique des contrôles de bornes. Il comprend notamment la borne de Tsirelson et vérifie qu’une valeur annoncée reste dans le domaine attendu par le contrat physique déclaré.

### `ids` — identifiants persistants

Le module `ids` résout les DOI et autres identifiants enregistrés. Il distingue un identifiant existant d’une revalidation en temps réel du contenu associé.

### `report` — rapports complets

Le module `report` génère des rapports d’audit structurés. Une section vide ou un élément non documenté ne doit pas être confondu avec une validation.

### `__main__` — commande d’exécution

Le point d’entrée `__main__` rassemble les contrôles afin de proposer une interface reproductible et explicite.

## 6. Utilisation en ligne de commande

Les commandes suivantes illustrent les principaux contrôles :

```bash
python -m ratiss audit --url <url> --sha256 <hash>     # intégrité d'un artefact servi
python -m ratiss audit-zenodo --record <id> --file <f> # checksum publié vs octets servis
python -m ratiss doi <doi>                             # résolution d'identifiant (Hérité 2)
python -m ratiss chsh <valeur>                         # borne de Tsirelson |S| ≤ 2√2
```

Les paramètres doivent être déclarés avant l’exécution. Les valeurs produites sont ensuite associées aux manifestes, aux journaux et aux reçus correspondants.

## 7. Architecture de l’écosystème RATISS

L’écosystème repose sur deux produits complémentaires :

- **Couche 1 — RATISS-Framework :** protocole d’audit exécutable, juge, scellement, provenance et rapports.
- **Couche 2 — RATISS-LABS-GTT :** plateforme expérimentale en neuf couches consacrée à la topologie, aux modèles du monde, à la simulation et aux visualisations.

La couche 1 juge la couche 2. Cette direction est un élément de gouvernance technique : les résultats de GTT doivent pouvoir être rejoués et évalués par un mécanisme distinct de la couche qui les produit.

Les artefacts qui n’entrent pas dans la chaîne principale ne sont pas effacés par défaut. Ils sont gelés, datés et documentés dans les mécanismes de provenance et d’orphelins.

## 8. État de RATISS-LABS-GTT

![Architecture à deux couches](docs/img/architecture-deux-couches.png)

![Preuve de concept des audits externes](docs/img/poc-externe-2026-09-13.png)

À l’état **2026-09-13**, les deux couches sont opérationnelles. Le juge analyse GTT en intégration continue à chaque push par dépendance Git scellée, au moyen de manifestes comparés à `SEALS.json`.

| Élément GTT | Valeur | Vérification |
|---|---:|---|
| Phases construites | 1–7 (relais Rouge divulgué, auditeur ⏳ EN ATTENTE) | `docs/AUDIT_TRAIL.md` de GTT |
| Tests | 108 passed, bibliothèque standard seule | CI `gtt.yml` |
| Juge de ce dépôt | exit 0 sur GTT | job CI `judge` |
| Run externe réel LeWM/TwoRooms | delta **0.626131533384**, APPROVED | certification GTT byte-identique |
| Rejeu indépendant | kit en une commande fourni | `docs/AUDIT-INDEPENDANT-KIT.md` de GTT |

La méthode de ce dépôt n’affirme rien sur GTT que GTT ne puisse rejouer. Cette contrainte est le contrat entre les deux produits.

## 9. Preuve de concept — 10 runs externes

La preuve de concept du **2026-09-13** couvre plusieurs catégories de contrôles :

| Plateforme | Cibles | Verdicts |
|---|---|---:|
| Zenodo | 4 fichiers servis comparés aux checksums md5 publiés, dont un article de chimie de **1856** | 4 CONFORMES |
| PyPI | wheels `openai` et `requests` comparées aux digests sha256 publiés | 2 CONFORMES |
| DOI / Crossref | 3 identifiants réels dont la résolution est vérifiée | 3 RESOUT |
| Contrôle négatif | digest `openai` appliqué à la wheel `requests` | **1 DIVERGENCE DÉTECTÉE** |

Le contrôle négatif est indispensable. Une méthode qui ne sait produire que des résultats conformes ne permet pas de distinguer une vérification effective d’un mécanisme toujours permissif.

Le run spécial millénaire du **2026-09-13** examine la revendication OpenAI Navier–Stokes. Le papier est scellé, le dépôt Lean est scellé au commit et le registre Clay est consulté. Aucune résolution n’est décernée. Les préprints concurrents ne sont pas atteignables par identifiant stable. Les détails figurent dans [`proofs/POC-MILLENAIRE-2026-09-13.md`](proofs/POC-MILLENAIRE-2026-09-13.md), et la portée complète dans [`proofs/POC-EXTERNAL-AUDITS-2026-09-13.md`](proofs/POC-EXTERNAL-AUDITS-2026-09-13.md).

## 10. Installation et reproduction

Le dépôt exige Python **>=3.9** et ne nécessite aucune dépendance externe pour les tests hors ligne.

```bash
git clone https://github.com/jonathansearch/RATISS-Framework.git
cd RATISS-Framework
python3 -m pytest -q                 # 47 tests hors-ligne, stdlib seule
python3 -m pytest -q --run-network   # + 4 tests réseau marqués
bash proofs/replay_poc.sh            # les 10 runs externes, une commande
```

Les tests réseau doivent être exécutés dans un environnement autorisant les connexions sortantes. Les résultats doivent être interprétés avec les journaux et les rapports associés, et non comme une garantie générale indépendante du contexte d’exécution.

## 11. Provenance et traçabilité

Chaque module porte sa ligne de provenance dans [`audit/PROVENANCE.md`](audit/PROVENANCE.md). Cette ligne précise le dépôt source, le commit source, l’existence éventuelle d’une réécriture ou d’une copie et l’auditeur nommé.

Un module sans provenance est refusé. Un auditeur prérempli est également refusé : la valeur reste **EN ATTENTE** jusqu’au visa de l’équipe Rouge conformément à la règle N2.

Le journal des déviations est conservé dans [`audit/journal-deviations.jsonl`](audit/journal-deviations.jsonl). Les rapports d’exemple sont disponibles dans [`examples/`](examples/) et les preuves de rejeu dans [`proofs/`](proofs/).

## 12. Interprétation des verdicts

Un verdict **CONFORME** signifie que le contrôle défini a été exécuté et que l’artefact satisfait le contrat technique annoncé pour ce contrôle. Il ne signifie pas que toutes les propriétés scientifiques possibles de l’artefact sont établies.

Un verdict **RESOUT** signifie que l’identifiant a été résolu selon le mécanisme prévu. Il ne signifie pas que le contenu a été revalidé expérimentalement.

Une **DIVERGENCE** est un résultat utile. Elle indique que l’artefact reçu ne correspond pas au hash ou à la condition attendue. La conserver dans le rapport protège l’intégrité du processus.

## 13. Licence et citation

Le projet est distribué sous licence MIT. Copyright (c) **2026 Jonathan Evina, RATISS Labs**. Consultez [`LICENSE`](LICENSE) pour le texte intégral et [`CITATION.cff`](CITATION.cff) pour les métadonnées de citation.

## Références

[1]: https://github.com/jonathansearch/RATISS-Framework "RATISS-Framework — protocole d’audit scientifique exécutable"
[2]: https://github.com/jonathansearch/RATISS-LABS-GTT "RATISS-LABS-GTT — plateforme expérimentale principale"
[3]: https://orcid.org/0009-0000-4092-5313 "ORCID de Jonathan Evina"

---

**La crédibilité d’un résultat dépend aussi de la capacité à documenter ses limites, ses écarts et ses conditions de reproduction.**

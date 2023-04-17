import streamlit as st
import matplotlib.pyplot as plt

st.title('Calculatrice de budget')

st.sidebar.title('Entrez les montants')

st.sidebar.title('Les revenus')
revenus = st.sidebar.number_input('Quels sont vos revenues mensuels nets?')
revenus_a = revenus * 12
revenus_h = revenus / 4

st.header('Vos revenus')
st.write('Vos revenus hebdomadaires nets sont:', revenus_h, '$')
st.write('Vos revenus mensuels nets sont:', revenus,'$')
st.write('Vos revenus annuels nets sont:', revenus_a, '$')
st.divider()

categories = ['logement ou hypothèque', 'électricité', 'paiement de voiture', 'essence', 'assurance', 'épicerie', 'contrat de téléphone', 'internet', 'abonnement', 'activités sportives', 'frais bancaires', 'restaurant', 'activités avec famille/amis', 'épargne', 'autres dépenses']

depenses_mensuelles = []
depenses_annuelles = []
depenses_hebdomadaires = []


st.sidebar.title('Les dépenses')
st.sidebar.write("Entrez vos dépenses sur une base mensuelle. Dans le cas où vous ne les connaissez seulement sur une base hebdomadaire ou annuelle, il est aussi possible de les inscrire dans les cases à cet effet. Cependant, ces dépenses ne seront pas prises en compte dans le graphique de vos dépenses mensuelles.\n\n ** Il est important d'inscrire vos dépenses pour chaque catégorie dans seulement une case (ne pas l'inscrire dans mensuelle, annuelle et hebdomadaire). **")
st.sidebar.header('Mensuellement')

for categorie in categories:
    mensuelle = st.sidebar.number_input(f'Mensuellement, combien dépensez-vous en {categorie}')
    
    depenses_mensuelles.append(mensuelle)

st.sidebar.divider()
st.sidebar.header('Annuellement')
    
for categoriee in categories:
    annuelle = st.sidebar.number_input(f'Annuellement, combien dépensez-vous en {categoriee}')
    
    depenses_annuelles.append(annuelle)
st.sidebar.divider()
st.sidebar.header('Hebdomadairement')

for categorih in categories:
    hebdomadaire = st.sidebar.number_input(f'Par semaine, combien dépensez-vous en {categorih}')
    depenses_hebdomadaires.append(hebdomadaire)


depense_mensuel = sum(depenses_mensuelles)
depense_annuelle = sum(depenses_annuelles)
depense_hebdomadaire = sum(depenses_hebdomadaires)

st.header("Vos dépenses")
st.write("Vos dépenses mensuelles s'élèvent à:", round(depense_mensuel, 2), "$")
st.write("Vos dépenses annuelles s'élèvent à:", round(depense_annuelle, 2), "$")
st.write("Vos dépenses hebdomadaires s'élèvent à:", round(depense_hebdomadaire, 2), "$")

labels = []
values = []

for i, categorie in enumerate(categories):
    mensuelle = depenses_mensuelles[i]
    if mensuelle > 0:
        labels.append(categorie)
        values.append(mensuelle)

fig1, ax1 = plt.subplots(facecolor = 'w', edgecolor = 'k')
ax1.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
ax1.set_title('Répartition des dépenses mensuelles par catégorie')

st.pyplot(fig1)

st.divider()

depensea = sum(depenses_annuelles) / 12
depenseh = sum(depenses_hebdomadaires) * 4
depenset = depensea + depenseh + sum(depenses_mensuelles)
resultat = revenus - depenset
epargne_sugg = revenus * .1
resultatdemi = resultat / 2



st.header('Les résulats :')
st.subheader(f"En calculant toutes vos dépenses de façon mensuel, vous dépensez {round(depenset, 2)}$ par mois.")

if resultat < 0:
    st.write(f"Vous êtes en déficit budgetaire à chaque mois de {round(resultat, 2)} $.")
    st.write(f"Voici quelques recommandations pour rétablir votre budget : \n\n - Restez discipliné : une fois que vous avez créé un plan de dépenses et que vous avez commencé à réduire vos dépenses et à augmenter vos revenus, continuez à suivre votre plan et à être discipliné avec votre argent.\n\n- Fixez des objectifs financiers : déterminez ce que vous voulez accomplir à court et à long terme, comme rembourser une dette ou épargner pour un achat important.\n\n- Créez un plan de dépenses : une fois que vous avez identifié vos domaines de dépenses, créez un plan de dépenses pour vous aider à réduire vos dépenses dans ces domaines. Vous pouvez utiliser une méthode d'enveloppe budgétaire pour allouer de l'argent à différentes catégories de dépenses.\n\n- Réduisez vos dépenses : cherchez des moyens de réduire vos dépenses, comme manger à la maison plutôt que de manger au restaurant, annuler des abonnements que vous n'utilisez pas, etc.")
             



elif resultat > 0:
    st.write(f"Bravo, vous avez un surplus budgétaire à la fin de chaque mois de {round(resultat, 2)} $.")
    st.write(f"Il est recommandé d'épargner 10% des revenues nets. \n\nPour vous, ce montant équivaut à {round(epargne_sugg, 2)} $ mensuellement.")
    st.write(f"Vous aussi pouvez épargner votre surplus en totalité ou épargnez seulement 50%. Dans ce cas, il vous restera tout de même {round(resultatdemi, 2)} $ à dépenser")








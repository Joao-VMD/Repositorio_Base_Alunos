import streamlit as st
import nota as nt
import numpy as np
import matplotlib.pyplot as plt

n_spikes = 600
np.random.seed(42)

fig = plt.figure(figsize=(6, 6), dpi=120)
ax = fig.add_subplot(111, polar=True)

ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])

angles = np.random.rand(n_spikes) * 2 * np.pi
lengths = np.random.exponential(scale=1.0, size=n_spikes) + np.random.normal(scale=0.15, size=n_spikes)
lengths = np.clip(lengths, 0, 6)

widths = 0.2 + (lengths / lengths.max()) * 3.5
cmap = plt.get_cmap('plasma')
colors = cmap(np.linspace(0, 1, n_spikes))

for i in range(n_spikes):
    a = angles[i] + np.random.normal(0, 0.12)
    r = lengths[i]
    lw = widths[i]
    alpha = 0.06 + 0.9 * (r / (lengths.max() + 1e-9)) ** 1.2
    ax.plot([a, a], [0, r], linewidth=lw, alpha=alpha, color=colors[i], solid_capstyle='round')

ax.scatter(angles, lengths, s=(5 + (lengths / lengths.max()) * 220), c=colors, alpha=0.9, linewidths=0)



st.image("https://divertidoanime.com/wp-content/uploads/2023/01/Classe_de_Iruka-1024x577.webp")
st.title("Shinobischool - Suas notas ninjas! 🥷😎")
st.caption("Criado com PACIENCIA")
nota1 = st.number_input("Digite a nota 1",min_value=0.0,max_value=10.0)
nota2 = st.number_input("Digite a nota 2",min_value=0.0,max_value=10.0)
nota3 = st.number_input("Digite a nota 3",min_value=0.0,max_value=10.0)
nota4 = st.number_input("Digite a nota 4",min_value=0.0,max_value=10.0)
botao = st.button("Colocar notas")
if botao:
    media= nt.calcular_media(nota1,nota2,nota3,nota4)
    situaçao= nt.situaçao(media)
    if situaçao =="aprovado":
        st.success(f"{situaçao}\n{media:.2f}")
        st.balloons()
    elif situaçao =="recuperação":
        st.warning(f"{situaçao}\n{media:.2f}")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPjoli7FuHAnBzqV33aCEsV4YQ2uegiCnhDg&s")
    elif situaçao == "reprovado":
        st.error(f"{situaçao}\n{media:.2f}")
        st.pyplot(fig)


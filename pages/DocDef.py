import streamlit as st

st.set_page_config(layout="wide", page_title="Definiciones documentadas", page_icon=":books:", initial_sidebar_state="collapsed")

st.title("Definiciones documentadas")
st.divider()
'''
En esta sección se encuentran segmentos de las multiples fuentes consultadas, contemplando que las primeras fueron
libros y desafortunadamente no es practico poner multiples segmentos del libro.

'''
st.subheader("Radiation Detection and Measurement")

r'''
La única radiación ionizante significativa producida por la desintegración beta es el electrón rápido o partícula beta en sí.
Porque la mayoría de los radionúclidos producidos por el bombardeo de neutrones de materiales estables son beta-activo,
una gran variedad de emisores beta son fácilmente disponibles a través de la producción en un flujo de reactor.
Se pueden obtener **especies con muchas vidas medias diferentes** , que van desde miles de años hasta una vida
media tan corta como sea práctico en la aplicación. La mayoría de las desintegraciones beta va de  un estado excitado
del núcleo del producto, de modo que la desexcitación posterior los rayos gamma se emiten junto con las partículas
beta en muchas fuentes beta comunes.
Cada transición de desintegración beta específica se caracteriza por una **energía de desintegración fija o valor Q.**
Debido a que la energía del núcleo de retroceso es prácticamente cero, esta energía se comparte entre el partícula beta
y el neutrino "invisible". La **partícula beta** aparece así con una energía que **varía de decaimiento en
decaimiento** y puede variar de cero a la "energía del punto final beta".
El valor $Q$ para un decaimiento dado se cita normalmente asumiendo que **la transición tiene lugar entre los
estados fundamentales de los núcleos padre e hija.** Si la transición implica un estado excitado del padre o de la hija,
la energía del punto final del espectro beta correspondiente será cambiado por la **diferencia en las energías de
excitación.**
Dado que varios estados excitados pueden ser poblados en algunos esquemas de desintegración, el espectro de partículas
beta medido puede consistir en varios componentes con diferentes energías de punto final.
'''

st.subheader("INTRODUCTORY NUCLEAR PHYSICS")

r'''
En la desintegración beta negativa no hay tal barrera para penetrar e incluso en la desintegración $\beta^+$, es posible
mostrar incluso desde un cálculo aproximado que el factor exponencial en la probabilidad de penetración de barrera es de
unidad de orden. Hay otras diferencias importantes entre el  decaimiento $\alpha$ y $\beta$ que nos sugieren que debemos
utilizar un enfoque completamente diferente para el cálculo de las probabilidades de transición en decaimiento
$\beta$: (1) El electrón y el neutrino no existen antes del proceso de decaimiento, y por lo tanto debemos explicar
la formación de esas partículas. (2) El electrón y el neutrino deben ser tratados de manera relativista. (3)
La distribución continua de las energías de los electrones debe resultar del cálculo.

En 1934, Fermi desarrolló una teoría exitosa de la desintegración $\beta$ basada en la hipótesis del neutrino de Pauli.
Las características esenciales de la desintegración pueden derivarse de la expresión básica de la probabilidad de
transición causada por una interacción que es débil en comparación con la interacción que forma los estados cuasi
estacionarios. Esto es ciertamente cierto para el decaimiento $\beta$, en el que los tiempos característicos
(las semividas, típicamente de segundos de orden o más) son mucho más largos que el tiempo nuclear característico
(10 -20 s). El resultado de este cálculo, tratando la interacción causante de decaimiento como una perturbación débil,
es la Regla de Oro de Fermi, un resultado general para cualquier tasa de transición previamente dada en la Ecuación 2.79:
$$
\lambda=\frac{2 \pi}{\hbar}\left|V_{\mathrm{fi}}\right|^2 \rho\left(E_{\mathrm{f}}\right)
$$

El elemento de la matiz $V_{\mathrm{fi}}$ es la integral de la interacción $V$ entre los estados cuasi estacionarios
inicial y final del sistema:
$$
V_{\mathrm{fi}}=\int \psi_{\mathrm{f}}^* V \psi_{\mathrm{i}} d v
$$

El factor $\rho\left(E_{\mathrm{f}}\right)$ es la densidad de los estados finales, que también se puede escribir como
$d n / d E_{\mathrm{f}}$, el numero $d n$ de estados finales en el intervalo de energía $d E_{\mathrm{f}}$.
Es más probable que se produzca una transición determinada si hay un gran número de estados finales accesibles.

Fermi no conocía la forma matemática de $V$ por la desintegración $\beta$  que hubiera permitido cálculos usando las
Ecuaciones 9.12 y 9.13. En cambio, consideró todas las formas posibles consistentes con la relatividad especial,
y mostró que $V$ podría ser reemplazado por uno de los cinco operadores matemáticos $O_X$, donde el subíndice $X$ da
la forma del operador $O$ (es decir, sus propiedades de transformación): $X=\mathrm{V}$ (vector), $A$ (vector axial),
$S$ (escalar), $\mathrm{P}$ (pseudoscalar), o $\mathrm{T}$ (tensor).



'''



st.subheader("Desintegración beta - Labster, s. f.")
r'''
La desintegración beta es un tipo de desintegración radiactiva por la cual un isótopo estable emite un electrón muy
rápido y energético (una partícula beta) para equilibrar la proporción de protones y neutrones en el núcleo.

En este tipo de desintegración, un neutrón del núcleo se convierte en un protón y un electrón muy energético. Dicho
electrón, generado en el núcleo, es expulsado de él en un estado de alta energía.
En la desintegración beta, la masa atómica es prácticamente constante (solo se pierde un electrón), mientras que el
número atómico se reduce en una unidad. La pérdida de masa total es menor que en la desintegración alfa, ya que solo
se expulsa un electrón del átomo. Esto ocurre, por ejemplo, con el nitrógeno-12. Un protón del nitrógeno-12 (Z=7) se
convierte en un neutrón, lo que genera un átomo de carbono-12 (Z=6) y provoca la emisión de un
electrón desde el núcleo (una partícula beta).

'''


st.subheader("Desintegración Beta, s. f.")

r'''
La desintegración beta, emisión beta o decaimiento beta es un proceso mediante el cual un nucleido inestable emite
una partícula beta para optimizar la relación N/Z (neutrones/protones) del núcleo. La partícula beta puede ser un
electrón, escribiéndose $\beta-$, o un positrón, $\beta+$. En la emisión beta, varían el número de protones y el de
neutrones del núcleo resultante, mientras que la suma de ambos (el número másico) permanece constante.

La diferencia fundamental entre un electrón o positrón y la partícula beta correspondiente es su origen nuclear: no se
trata de un electrón ordinario arrancado de un orbital atómico.

Una reacción alternativa que hace que un núcleo con exceso de protones se vuelva más estable es la captura electrónica.

'''

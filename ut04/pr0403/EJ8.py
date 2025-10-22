nombres = [
    "Alejandro", "María", "Javier", "Lucía", "Carlos", "Sofía", "Miguel", "Ana", "Manuel", "Isabel", "Pedro", "Carmen", "Jorge", "Elena", "Juan", "Laura", "Antonio", "Patricia", "David", "Claudia", "Francisco", "Marta", "Sergio", "Teresa", "Luis", "Raquel", "Andrés", "Paula", "Daniel", "Verónica", "Fernando", "Sara", "Pablo", "Irene", "Álvaro", "Natalia", "Hugo", "Eva", "Diego", "Cristina", "Jesús", "Rosa", "Roberto", "Alicia", "Ángel", "Beatriz", "Ricardo", "Julia", "Adrián", "Silvia", "Alberto", "Victoria", "Raúl", "Pilar", "Ramón", "Lidia", "Óscar", "Ariadna", "Gonzalo", "Mónica", "Rubén", "Esther", "Santiago", "Nuria", "Iván", "Ainhoa", "Eduardo", "Berta", "Marcos", "Noelia", "Enrique", "Elisa", "Emilio", "Fátima", "Vicente", "Gabriela", "Mario", "Olga", "Rafael", "Lorena", "Mariano", "Cristina", "Eugenio", "Mercedes", "Félix", "Amparo", "Sebastián", "Rocío", "Alfredo", "Esperanza", "Álex", "Celia", "Héctor", "Andrea", "Tomás", "Inés", "Marcelo", "Gloria", "Marina", "Belén", "Valentín", "Miriam", "Guillermo", "Ángela", "Joaquín", "Gemma", "Fabián", "Daniela", "Víctor", "Dolores", "Marcos", "Tamara", "Braulio", "Lourdes", "Federico", "Gema", "Julián", "Nicolás", "Leandro", "Manuela", "Agustín", "Elsa", "Julio", "Consuelo", "Ismael", "Alejandra", "Joaquín", "Milagros", "Gregorio", "Inmaculada", "Salvador", "Carla", "Esteban", "Carolina", "Fausto", "Emilia", "Alfonso", "Amalia", "Baltasar", "Adela", "Humberto", "Blanca", "Aníbal", "Araceli", "César", "Candela"
]
A = B = C = D = E = F = G = H = I = J = K = L = M = N = Ñ = O = P = Q = R = S = T = U = V = W = X = Y = Z = 0
a_set = {"A", "a", "á", "Á"}
b_set = {"B", "b"}
c_set = {"C", "c"}
d_set = {"D", "d"}
e_set = {"E", "e", "é", "É"}
f_set = {"F", "f"}
g_set = {"G", "g"}
h_set = {"H", "h"}
i_set = {"I", "i", "í", "Í"}
j_set = {"J", "j"}
k_set = {"K", "k"}
l_set = {"L", "l"}
m_set = {"M", "m"}
n_set = {"N", "n"}
ñ_set = {"Ñ", "ñ"}
o_set = {"O", "o", "ó", "Ó"}
p_set = {"P", "p"}
q_set = {"Q", "q"}
r_set = {"R", "r"}
s_set = {"S", "s"}
t_set = {"T", "t"}
u_set = {"U", "u", "ú", "Ú"}
v_set = {"V", "v"}
w_set = {"W", "w"}
x_set = {"X", "x"}
y_set = {"Y", "y"}
z_set = {"Z", "z"}
for nombre in nombres:
    for c in nombre:
        if c in a_set:
            A += 1
        elif c in b_set:
            B += 1
        elif c in c_set:
            C += 1
        elif c in d_set:
            D += 1
        elif c in e_set:
            E += 1
        elif c in f_set:
            F += 1
        elif c in g_set:
            G += 1
        elif c in h_set:
            H += 1
        elif c in i_set:
            I += 1
        elif c in j_set:
            J += 1
        elif c in k_set:
            K += 1
        elif c in l_set:
            L += 1
        elif c in m_set:
            M += 1
        elif c in n_set:
            N += 1
        elif c in ñ_set:
            Ñ += 1
        elif c in o_set:
            O += 1
        elif c in p_set:
            P += 1
        elif c in q_set:
            Q += 1
        elif c in r_set:
            R += 1
        elif c in s_set:
            S += 1
        elif c in t_set:
            T += 1
        elif c in u_set:
            U += 1
        elif c in v_set:
            V += 1
        elif c in w_set:
            W += 1
        elif c in x_set:
            X += 1
        elif c in y_set:
            Y += 1
        elif c in z_set:
            Z += 1
print("Conteo letras:")
print(f"A: {A}  B: {B}  C: {C}  D: {D}  E: {E}  F: {F}  G: {G}  H: {H}  I: {I}  J: {J}")
print(f"K: {K}  L: {L}  M: {M}  N: {N}  Ñ: {Ñ}  O: {O}  P: {P}  Q: {Q}  R: {R}  S: {S}")
print(f"T: {T}  U: {U}  V: {V}  W: {W}  X: {X}  Y: {Y}  Z: {Z}")

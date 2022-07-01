import numpy as np
import matplotlib.pyplot as plt
number_of_particles=200
number_of_iterations=100
w=0.95
c1=1.494
c2=1.494
delta_t=0.01
positions_matrix=np.zeros((number_of_particles,2))
velocities_matrix=np.zeros((number_of_particles,2))
current_values_matrix=0
personel_bests_matrix=np.ones((number_of_particles,2))
personel_bests_values_array=np.ones(number_of_particles)*999
gbest=0
val_gbest=999
values=np.ones(number_of_particles)*999
alt_sinir_x=-15
ust_sinir_x=15
alt_sinir_y=-15
ust_sinir_y=15
alt_sinir_v_x=-1
ust_sinir_v_x=1
alt_sinir_v_y=-1
ust_sinir_v_y=1
def ParcaciklariIlklendir(alt_sinir_x, ust_sinir_x, alt_sinir_y, ust_sinir_y, alt_sinir_v_x, ust_sinir_v_x, alt_sinir_v_y, ust_sinir_v_y):  

    global positions_matrix,velocities_matrix
    for i in range(number_of_particles):
        position_x=np.random.randint(alt_sinir_x,ust_sinir_x-1)+np.random.rand()
        position_y=np.random.randint(alt_sinir_y,ust_sinir_y-1)+np.random.rand()
        velocity_x=np.random.randint(alt_sinir_v_x,ust_sinir_v_x-1)+np.random.rand()
        velocity_y=np.random.randint(alt_sinir_v_y,ust_sinir_v_y-1)+np.random.rand()
        positions_matrix[i]=[position_x,position_y]
        velocities_matrix[i]=[velocity_x,velocity_y]
    

def AmacFonksiyonuHesapla(x,y):
    return (x-10)*(x-10)+(y-10)*(y-10)

def BirParcacigiGuncelle (i, w, c1, c2, delta_t):
    r1_x=np.random.rand()
    r1_y= np.random.rand()
    r1=np.array([r1_x,r1_y])
    r2_x=np.random.rand()
    r2_y = np.random.rand()
    r2 = np.array([r2_x, r2_y])
    global gbest,values,positions_matrix,velocities_matrix,val_gbest,personel_bests_matrix,positions_matrix
    velocities_matrix[i]=(w*velocities_matrix[i])+(c1*r1*(personel_bests_matrix[i]-positions_matrix[i]))+(c2*r2*(gbest-positions_matrix[i]))
    positions_matrix[i]=positions_matrix[i]+(velocities_matrix[i]*delta_t)
    print("---" * 20)

    x=positions_matrix[i][0]
    y=positions_matrix[i][1]

    value=AmacFonksiyonuHesapla(x,y)

    values[i]=value
    print(personel_bests_values_array,value,val_gbest,np.min(values))

    if  personel_bests_values_array[i]>value:
        personel_bests_values_array[i]=value
        personel_bests_matrix[i]=positions_matrix[i]
    if val_gbest>np.min(values):
        gbest=positions_matrix[np.argmin(values)]
        val_gbest=np.min(values)


def TumParcaciklariGuncelle (number_of_particles):
    for i in range(number_of_particles):
        BirParcacigiGuncelle(i,w,c1,c2,delta_t)


def TumParcacikKonumlariniCizdir (number_of_particles):
    _positions_matrix=np.array(positions_matrix).transpose()
    plt.xlim([-20,20])
    plt.ylim([-20,20])
    plt.scatter(_positions_matrix[0],_positions_matrix[1])
    plt.pause(0.001)
    
def PerformParticleSwarmOptimization(number_of_particles, number_of_iterations, w, c1, c2, delta_t, alt_sinir_x, ust_sinir_x, alt_sinir_y, ust_sinir_y, alt_sinir_v_x, ust_sinir_v_x, alt_sinir_v_y, ust_sinir_v_y):
    global positions_matrix,velocities_matrix
    ParcaciklariIlklendir (alt_sinir_x, ust_sinir_x, alt_sinir_y, ust_sinir_y, alt_sinir_v_x, ust_sinir_v_x,alt_sinir_v_y, ust_sinir_v_y)
    for a in range(number_of_iterations):
        plt.clf()
        w=w-(0.94-0.4)/number_of_iterations*0.5
        TumParcaciklariGuncelle (number_of_particles)
        TumParcacikKonumlariniCizdir(number_of_particles)


PerformParticleSwarmOptimization(number_of_particles, number_of_iterations, w, c1, c2, delta_t, alt_sinir_x, ust_sinir_x, alt_sinir_y, ust_sinir_y, alt_sinir_v_x, ust_sinir_v_x, alt_sinir_v_y, ust_sinir_v_y)
plt.show()
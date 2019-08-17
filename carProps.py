import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

class carProps:
    def __init__(self,m,r_d,rpm,torque,angle,L,a,f_r,c_x,A_f,rho,v, i_D, rpm_topSpeed,z):
        # User inputs:
        self.m = m
        self.r_d = r_d
        self.rpm = np.array(rpm)
        self.torque = np.array(torque)
        self.angle = angle
        self.i_D = i_D
        self.rpm_topSpeed = rpm_topSpeed
        self.z = z

        # Constants
        self.g = 9.8
        self.rpm2rad = 0.104719755120
        self.rad2rpm =  9.549296585514
        
        # Power Curves
        self.powerInW = self.torque*self.rpm*self.rpm2rad
        self.powerInHP = self.powerInW/745.7
        
        # Coefficient for Rotational Inertica Calculations
        self.L = L
        self.a = a*self.g
        
        # Coefficients for Rolling Resistance Calculations
        self.f_r = f_r
        self.G_r = self.m
         
        # Coefficients for Drag Calculations
        self.c_x = c_x
        self.A_f = A_f
        self.rho = rho
        self.v = v/3.6

        # Calculates inertial resistance values
        self.F_I = self.L*self.m*self.a

        # Calculates Rolling Resistance
        self.F_R = self.f_r*self.G_r
        
        # Calculates Drag Resistance
        self.vecVel = np.linspace(0,self.v*1.2,int(self.v*1.2))

        # Drag @ max. Speed
        self.F_D_max = 0.5*self.rho*self.c_x*self.A_f*self.v*self.v
         
        # Calculates Ramp Resistance
        rad = math.radians(self.angle)
        self.F_A = self.m*self.g*np.sin(rad)

        # Resistances for first gear
        
        # Force
        F_i1 = self.F_I+self.F_R+self.F_A
        
        # Torque
        T_i1 = F_i1*self.r_d

        # Max Engine Torque
        T_max = max(self.torque)

        # Total ratio for first gear
        i1_total = T_i1/T_max

        # First gear
        self.i1 = i1_total/self.i_D

        # Last gear
        self.ilast = (((3.6*3.14/30)*self.rpm_topSpeed*self.r_d)/v)/self.i_D

        # Theoretical Topspeed
        self.topSpeed = self.rpm_topSpeed*self.rpm2rad*self.r_d*3.6/(self.ilast*self.i_D)

        # Gear ratios
        self.i = []
        for x in range(0,self.z):
            self.i.append(0)

        # Overall Gear Ratio
        i_G = self.i1/self.ilast

        # Constant 2
        phi2 = 1.0

        # Constant 1
        div = pow(phi2,0.5*(z-1)*(z-2))
        phi1 = pow(i_G/div,1/(z-1))

        for n in range(1,z+1):
            exp1 = (z-n)
            exp2 = 0.5*(z-n)*(z-n-1)
            self.i[n-1] = self.ilast*pow(phi1,exp1)*pow(phi2,exp2)

    def plotTorque(self):

        self.T_D = ((0.5*self.rho*self.c_x*self.A_f*self.vecVel*self.vecVel)*self.r_d)/(self.ilast*self.i_D)
        self.v_D = (self.vecVel/self.r_d)*self.rad2rpm*(self.ilast*self.i_D)

        self.figTorque = plt.Figure(figsize=(8,5))
        a = self.figTorque.add_subplot(111)
        a.plot(self.rpm, self.torque, self.v_D, self.T_D)
        a.set_xlim([self.rpm[0],self.rpm[len(self.rpm)-1]])
        a.set_xlabel('Engine Revs (RPM)')
        a.set_ylabel('Torque (Nm)')
        a.set_title('Engine Torque and Resistance')
        a.legend(['Engine torque output','Resistance torque at last gear'])
        a.grid()

    def plotPower(self):
        self.P_D = self.vecVel*self.T_D/(self.r_d*745.7)*(self.ilast*self.i_D)
        self.figPower = plt.Figure(figsize=(8,5))
        a = self.figPower.add_subplot(111)
        a.plot(self.rpm, self.powerInHP, self.v_D, self.P_D)
        a.set_xlim([self.rpm[0],self.rpm[len(self.rpm)-1]])
        a.set_xlabel('Engine Revs (RPM)')
        a.set_ylabel('Power (HP)')
        a.set_title('Engine Power and Resistance')
        a.legend(['Engine power output','Resistance power at last gear'])
        a.grid()

    def speedMap(self):

        caps = []
        speedMap = np.zeros((len(self.i),len(self.rpm)))
        
        for x in range(0,len(self.i)):
            caps.append('Gear '+str(x+1))
            speedMap[x,:]=((3.6*3.14/30)*self.rpm*self.r_d / (self.i[x]*self.i_D))
        
        self.figSpeedMap = plt.Figure(figsize=(8,5))
        
        a = self.figSpeedMap.add_subplot(111)
        a.plot(np.transpose(speedMap[:]),self.rpm)
        a.set_xlabel('Speed (km/h)')
        a.set_ylabel('Engine Revs (RPM)')
        a.set_title('Speed Map')
        a.legend(caps)
        a.grid()

    def tractiveForces(self):
        
        caps = []
        forces = np.zeros((len(self.i),len(self.rpm)))
        speed = np.zeros((len(self.i),len(self.rpm)))
        
        for x in range(0,len(self.i)):
            caps.append('Gear '+str(x+1))
            forces[x,:] = self.torque*(self.i[x]*self.i_D)/self.r_d
            speed[x,:] = (3.6*3.14/30)*self.rpm*self.r_d /(self.i[x]*self.i_D)
        
        self.figTractiveForces = plt.Figure(figsize=(8,5))
        
        a = self.figTractiveForces.add_subplot(111)
        a.plot(np.transpose(speed[:]), np.transpose(forces[:]))
        a.set_xlabel('Speed (km/h)')
        a.set_ylabel('Traction Force (N)')
        a.set_title('Traction capabilities')
        a.legend(caps)
        a.grid()
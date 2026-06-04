#Esse é meu primeiro projeto, vindo do freeCodeCamp. A ideia é: enquanto prossigo no curso, projetos vão
#surgindo. Eu irei replicar esses projetos do meu jeito, manualmente, enquanto subo pro GitHub.
#Os projetos, o inglês e o GitHub terão erros, vindos da minha inexperiência, mas também fará visível a 
#minha evolução. 

#Recebe inputs do usuário
name = input("Write your full name: ")
age = input("How old are you? ")
score = input("How much do you get on the exam? ")

#Printa inputs
print(f"Hi, {name}.")
print(f"{name}, you are {age} years old and get {score} in the exam.")

#Faz a lógica if para determinar aprovação
if int(score) >= 70:
    print("You are approved!")
else:
    print("Not approved.")
print("""
  ______             __                                               
 /      \           /  |                                              
/$$$$$$  |  _______ $$ |____    ______          ______                
$$ |__$$ | /       |$$      \  /      \        /      \               
$$    $$ |/$$$$$$$/ $$$$$$$  |/$$$$$$  |      /$$$$$$  |              
$$$$$$$$ |$$ |      $$ |  $$ |$$    $$ |      $$ |  $$ |              
$$ |  $$ |$$ \_____ $$ |  $$ |$$$$$$$$/       $$ \__$$ |              
$$ |  $$ |$$       |$$ |  $$ |$$       |      $$    $$/               
$$/   $$/  $$$$$$$/ $$/   $$/  $$$$$$$/        $$$$$$/                
 ________                                                             
/        |                                                            
$$$$$$$$/   ______    _______   ______   __    __   ______    ______  
   $$ |    /      \  /       | /      \ /  |  /  | /      \  /      \ 
   $$ |   /$$$$$$  |/$$$$$$$/ /$$$$$$  |$$ |  $$ |/$$$$$$  |/$$$$$$  |
   $$ |   $$    $$ |$$      \ $$ |  $$ |$$ |  $$ |$$ |  $$/ $$ |  $$ |
   $$ |   $$$$$$$$/  $$$$$$  |$$ \__$$ |$$ \__$$ |$$ |      $$ \__$$ |
   $$ |   $$       |/     $$/ $$    $$/ $$    $$/ $$ |      $$    $$/ 
   $$/     $$$$$$$/ $$$$$$$/   $$$$$$/   $$$$$$/  $$/        $$$$$$/  
                                                                      
""")
print("Você acabou de chegar na ilha do tesouro. pegue seu mapa e escolha ir para direita ou esquerda para achar o tesouro.\n\n\n")
first_question = input("Você deseja ir para D/E?\n").upper()
if first_question == "D":
    print("\n\033[92mMuito Bem!\033[0m\n")

    second_question = input(
        "\nVocê chegou a base da montanha e precisa tomar uma decisão. D/E/ESC(escalar)\n").upper()
    if second_question == "ESC":
        print(
            "\n\033[91mVocê decidiu escalar, mas sua corda quebrou e voce morreu.\033[0m")
    elif second_question == "E":
        print(
            "\n\033[92mParabéns! Você foi pela esquerda e acabou encontrando o rio.\033[0m\n")
        third_question = input(
            "\nEscolha a melhor opcao. Voce está bem perto! N(nadar)/A(arvore)/B(Barco)\n").upper()
        if third_question == "A":
            print(
                "\n\033[92mVoce Acabou de achar a caverna do tesouro!!\033[0m")
            print("""

            _______                               __                                     
            /       \                             /  |                                    
            $$$$$$$  | ______    ______   ______  $$ |____    ______   _______    _______ 
            $$ |__$$ |/      \  /      \ /      \ $$      \  /      \ /       \  /       |
            $$    $$/ $$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$$  |/$$$$$$$/ 
            $$$$$$$/  /    $$ |$$ |  $$/ /    $$ |$$ |  $$ |$$    $$ |$$ |  $$ |$$      \ 
            $$ |     /$$$$$$$ |$$ |     /$$$$$$$ |$$ |__$$ |$$$$$$$$/ $$ |  $$ | $$$$$$  |
            $$ |     $$    $$ |$$ |     $$    $$ |$$    $$/ $$       |$$ |  $$ |/     $$/ 
            $$/       $$$$$$$/ $$/       $$$$$$$/ $$$$$$$/   $$$$$$$/ $$/   $$/ $$$$$$$/  
                                                                                        
                                                                                        
                                                                                        
            """)
        elif third_question == "B":
            print(
                "\n\033[91mVocê escolheu ir de barco, mas afundo e morreu afogado.\033[0m")
        else:
            print(
                "\n\033[91mVocê escolheu nadar, mas os crocodilos ficaram de barriga cheia.\033[0m")

    else:
        print(
            "\n\033[91mVocê foi pela direita e acabou sendo morto por um leopardo.\033[0m")

else:
    print(
        "\n\033[91mVocê foi pela esquerda e acabou sendo morto por um dragão de comodo.\033[0m\n")

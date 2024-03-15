from langid.langid import LanguageIdentifier, model


def main():
    phrase = ""
    
    identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
    
    print("Escreva uma frase, ou 0 para sair")
    phrase = input()
    while phrase != "0":
        result = identifier.classify(phrase)
        print("Língua dectectada:", result[0])
        print("Escreva uma frase, ou 0 para sair")
        phrase = input()


if __name__ == "__main__":
    main()
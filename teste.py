from random import choice

area_subarea = [{'administrativo':
                choice(['operações administrativas', 'parcerias', 'comunicação', 'financeiro'])},
            {'aviônica':
                choice(['projetos aviônicos', 'acionamento', 'controle', 'energia', 'telemetria', 'aviônica', 'aviônica para foguetes'])},
            {'mecânica':
                choice(['projetos mecânicos', 'dinâmica de voo', 'propulsão', 'qualidade', 'estrutura', 'dinâmica de voo', 'simulação'])},
            {'pesquisa e extensão':
                choice(['pesquisa e extensão', 'extensão', 'pesquisa científica'])},
            {'computação':
            choice(['projetos computacionais', 'inteligência artificial', 'computação'])}]

def selecao1(cursos_campus):
    cursos_campus = [{'administração':
                choice(['curitiba', 'pato branco'])},
            {'agronomia':
                choice(['dois vizinhos', 'pato branco', 'santa helena'])},
            {'arquitetura e urbanismo':
                'curitiba'},
            {'bacharelado em engenharia de software':
                choice(['cornélio procópio', 'dois vizinhos'])},
            {'ciência da computação':
                choice(['campo mourão', 'medianeira', 'ponta grossa', 'santa helena'])},
            {'ciências contábeis':
                'pato branco'},
            {'comunicação organizacional':
                'curitiba'},
            {'design':
                'curitiba'},
            {'educação física':
                'curitiba'},
            {'engenharia ambiental':
                choice(['campo mourão', 'francisco beltrão', 'londrina', 'medianeira'])},
            {'engenharia ambiental e sanitária':
                'curitiba'},
            {'engenharia civil':
                choice(['apucarana', 'campo mourão', 'curitiba', 'guarapuava', 'pato branco', 'toledo'])},
            {'engenharia de alimentos':
                choice(['campo mourão', 'francisco beltrão', 'medianeira'])},
            {'engenharia de bioprocessos e biotecnologia':
                choice(['dois vizinhos', 'ponta grossa', 'toledo'])},
            {'engenharia de computação':
                choice(['apucarana', 'cornélio procópio', 'curitiba', 'pato branco', 'toledo'])},
            {'engenharia de controle e automação':
                choice(['cornélio procópio', 'curitiba'])},
            {'engenharia de materiais':
                'londrina'},
            {'engenharia de produção':
                choice(['londrina', 'medianeira', 'ponta grossa'])},
            {'engenharia elétrica':
                choice(['apucarana', 'cornélio procópio', 'curitiba', 'medianeira', 'pato branco', 'ponta grossa'])},
            {'engenharia eletrônica':
                choice(['campo mourão', 'cornélio procópio', 'curitiba', 'toledo'])},
            {'engenharia florestal':
                'dois vizinhos'},
            {'engenharia mecânica':
                choice(['cornélio procópio', 'curitiba', 'guarapuava', 'londrina', 'pato branco', 'ponta grossa'])},
            {'engenharia mecatrônica':
                'curitiba'},
            {'engenharia química':
                choice(['apucarana', 'campo mourão', 'francisco beltrão', 'londrina', 'ponta grossa'])},
            {'engenharia têxtil':
                'apucarana'},
            {'licenciatura em ciências biológicas':
                choice(['dois vizinhos', 'ponta grossa', 'santa helena'])},
            {'licenciatura em física':
                'curitiba'},
            {'licenciatura em informática':
                'francisco beltrão'},
            {'licenciatura em letras inglês':
                'curitiba'},
            {'licenciaturas em letras português e inglês':
                'pato branco'},
            {'licenciatura em letras português':
                'curitiba'},
            {'licenciatura em matemática':
                choice(['cornélio procópio', 'curitiba', 'pato branco', 'toledo'])},
            {'licenciatura em química':
                choice(['apucarana', 'campo mourão', 'curitiba', 'londrina', 'medianeira'])},
            {'química':
                choice(['curitiba', 'pato branco'])},
            {'sistema de informação':
                'curitiba'},
            {'tecnologia em alimentos':
                choice(['campo mourão', 'londrina', 'medianeira'])},
            {'tecnologia em análise e desenvolvimento de sistemas':
                choice(['cornélio procópio', 'pato branco', 'ponta grossa'])},
            {'tecnologia em automação industrial':
                choice(['curitiba', 'ponta grossa'])},
            {'tecnologia em design de moda':
                'apucarana'},
            {'tecnologia em design gráfico':
                'curitiba'},
            {'tecnologia em fabricação mecânica':
                'ponta grossa'},
            {'tecnologia em gestão ambiental':
                'medianeira'},
            {'tecnologia em manutenção industrial':
                choice(['guarapuava', 'medianeira', 'pato branco'])},
            {'tecnologia em processos químicos':
                'toledo'},
            {'tecnologia em radiologia':
                'curitiba'},
            {'tecnologia em sistemas para internet':
                choice(['guarapuava', 'toledo'])},
            {'zootecnia':
                'dois vizinhos'}]

    dados = choice(cursos_campus)
    return f"curso={str(dados.values())[14:-3].upper()}, campus={str(dados.keys())[12:-3].upper()}"


print(str(selecao1))
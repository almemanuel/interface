from names import get_full_name as name
from lorem import paragraph
from random import randrange, choice

class Pessoa:
    def __init__(self, curso = '', campus = '', area = '', subarea = ''):
        self.nome = name()
        self.email = self.nome.replace(" ", "").lower() + '@alunos.utfpr.edu.br'
        self.whatsapp = f'+55 {randrange(10, 99)} {90000 + randrange(0, 9999)}-{randrange(0, 9999):4}'
        self.ra = f'{randrange(0, 9999999):7}'
        self.curso = curso
        self.periodo = randrange(1, 10)
        self.campus = campus
        self.area = area
        self.subarea = subarea
        self.qualidades = paragraph()
        self.defeitos = paragraph()

    @staticmethod
    def gerar(quantidade = 1):
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

        curso = choice(cursos_campus)
        campus = str(curso.values())[14:-3].upper()
        curso = str(curso.keys())[12:-3].upper()
        area = choice(area_subarea)
        subarea = str(area.values())[14:-3].upper()
        area = str(area.keys())[12:-3].upper()

        return [Pessoa(curso, campus, area, subarea) for i in range(quantidade)]


    @staticmethod
    def mostrar(lista):
        print([str(candidato) for candidato in lista])


    def __str__(self):
        return f"[nome={self.nome}, email={self.email}, whatsapp={self.whatsapp}, ra={self.ra}, curso={self.curso}, periodo={self.periodo}, campus={self.campus}, area={self.area}, subarea={self.subarea}, qualidades={self.qualidades}, defeitos={self.defeitos}]"


lista = Pessoa.gerar(randrange(1, 10))
Pessoa.mostrar(lista)
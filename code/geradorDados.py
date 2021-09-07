from names import get_full_name as name
from lorem import paragraph
from random import randrange, choice

class Pessoa:
    """
    Classe contendo dados articiais para simular a interface de processo seletivo
    """
    def __init__(self, info_academica = [], info_orion = []):
        """Construtores da classe e formatação das strings
        Args:
            info_academica (list, opcional): lista com os cursos e os campus onde são ofertados.
            info_orion (list, opcional): lista com as áreas e suas respectivas subáreas.

        """
        self.nome = name()
        self.email = self.nome.replace(" ", "").lower() + '@alunos.utfpr.edu.br'
        self.whatsapp = f'+55 {randrange(10, 99)} {90000 + randrange(0, 9999)}-{(str(randrange(0, 9999))):0>4}'
        self.ra = f"{str(randrange(1, 9999999)):0<7}"
        self.curso = choice(info_academica)
        self.periodo = randrange(1, 10)
        self.campus = str(self.curso.values())[14:-3].capitalize()
        self.curso = str(self.curso.keys())[12:-3].capitalize()
        self.area = choice(info_orion)
        self.subarea = str(self.area.values())[14:-3].capitalize()
        self.area = str(self.area.keys())[12:-3].capitalize()
        self.qualidades = paragraph()
        self.defeitos = paragraph()
        self.resultado = 'Reprovado'


    @staticmethod
    def gerar(quantidade = 1):
        """geração dos dados

        Args:
            quantidade (int, opcional): quantidado de candidatos que será gerada artificialmete. Padrão é 1.

        Returns:
            list: lista com os dados gerados para os candidatos
        """
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
            {'análise e desenvolvimento de sistemas':
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
            {'pesquisa e Extensão':
                choice(['pesquisa e Extensão', 'extensão', 'pesquisa científica'])},
            {'computação':
                choice(['projetos computacionais', 'inteligência artificial', 'computação'])}]

        return [Pessoa(cursos_campus, area_subarea) for i in range(quantidade)]


    def __str__(self):
        """Padrão de string para o objeto

        Returns:
            string: dados gerados para os candidatos com a devida formatação
        """
        return f"{self.nome}, {self.email}, {self.whatsapp}, {self.ra}, {self.curso}, {self.periodo}, {self.campus}, {self.area}, {self.subarea}, {self.qualidades}, {self.defeitos}, {self.resultado}"


def gerar_e_salvar(file = 'candidatos', quantidade = randrange(1,100)):
    """Chamada para a geração dos dados e exportação para planilha

    Args:
        quantidade (int, opcional): quantidade de dados que será gerado e, consequentemente, de linhas na planilha. Padrão é qualquer valor aleatório no intervalo [1, 100].
    """
    planilha = Pessoa.gerar(quantidade)
    candidatos = open(file+'.csv', "w")
    candidatos.write("Nome, E-mail, WhatsApp, RA, Curso, Período, Campus, Área, Subarea, Qualidades, Defeitos, Resultado\n")
    for c in range(len(planilha)):
        candidatos.write(str(planilha[c]))
        candidatos.write('\n')
    candidatos.close()

# Programa Principal
if __name__ == "__main__": gerar_e_salvar()

from django.db import models
from datetime import datetime  

class Paciente(models.Model):
    nome_completo = models.CharField("Nome", max_length=512)
    data_nascimento = models.DateField("Data de nascimento")
    naturalidade = models.CharField("Naturalidade", max_length=512, blank=True)
    estado_civil = models.CharField("Estado civil", max_length=128, blank=True)
    numero_de_filhos = models.SmallIntegerField("Número de filhos", default=0, blank=True)
    mora_sozinho = models.CharField("Mora sozinho(a) ou com alguém?", max_length=512, blank=True)
    endereco = models.CharField("Endereço", max_length=512, blank=True)
    bairro = models.CharField("Bairro", max_length=512, blank=True)
    cidade = models.CharField("Cidade", max_length=512, blank=True)
    estado = models.CharField("Estado", max_length=128, blank=True)
    cep = models.CharField("CEP", max_length=10, blank=True)
    telefone = models.CharField("Telefone", max_length=32, blank=True)
    email = models.CharField("E-Mail", max_length=512, blank=True)
    rg = models.CharField("RG", max_length=32, blank=True)
    cpf = models.CharField("CPF", max_length=16, blank=True)
    lateralidade = models.CharField("Lateralidade", max_length=128, blank=True)
    escola = models.CharField("Escola", max_length=512, blank=True)
    serie = models.CharField("Série", max_length=128, blank=True)
    idade = models.CharField("Idade", max_length=128, blank=True)
    hd = models.CharField("HD", max_length=512, blank=True)
    relatorios = models.CharField("Relatórios", max_length=512, blank=True)
    nome_mae = models.CharField("Nome da mãe", max_length=512, blank=True)
    nome_pai = models.CharField("Nome do pai", max_length=512, blank=True)
    medico_nome_crm = models.CharField("Médico e CRM", max_length=512, blank=True)
    responsavel_telefone = models.CharField("Telefone", max_length=32, blank=True)
    responsavel_email = models.CharField("E-Mail", max_length=512, blank=True)
    responsavel_rg = models.CharField("RG", max_length=32, blank=True)
    responsavel_cpf = models.CharField("CPF", max_length=16, blank=True)
    religiao = models.TextField("Religião e crenças", blank=True)
    hobbies = models.TextField("Hobbies e atividades que pratica", blank=True)
    socializacao = models.TextField("Socialização e amizades", blank=True)
    estuda = models.CharField("Estuda no momento?", max_length=512, blank=True)
    estuda_periodo = models.CharField("Qual período?", max_length=512, blank=True)
    terapia_anterior_ja_fez = models.CharField("Já fez terapia antes?", max_length=512, blank=True)
    terapia_anterior_quanto_tempo = models.CharField("Se sim, por quanto tempo?", max_length=512, blank=True)
    expectativas = models.TextField("O que o/a paciente espera do processo de avaliação?", blank=True)
    objetivos = models.TextField("Quais os objetivos do(a) paciente com a avaliação", blank=True)

    def __str__(self):
        return self.nome_completo

class Anamnese(models.Model):
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    historia_de_vida = models.TextField("1 História de vida", blank=True)
    sintomas = models.TextField("2 Sintomas", blank=True)
    parte_e_gestacao = models.TextField("3 Parte e gestação", blank=True)
    desenvolvimento_psicomotor = models.TextField("4 Desenvolvimento psicomotor", blank=True)
    investigacoes = models.TextField("5 Investigações", blank=True)

    def __str__(self):
        return self.paciente.nome_completo


class Sessao(models.Model):
    class Meta:
        verbose_name_plural = "Sessões"
        verbose_name = "Sessão"
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    horario = models.DateTimeField("Horário da sessão", default=datetime.now)
    anotacoes = models.TextField("Anotações", blank=True)

    def __str__(self):
        return "%s - %s" % (self.paciente.nome_completo, self.horario.strftime("%d/%m/%Y %H:%M"))

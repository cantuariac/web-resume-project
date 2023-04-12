from django.core.management import BaseCommand

from resume.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        SocialMedia(name='LinkedIn',
                    base_url='https://www.linkedin.com/in/',
                    icon_color='0e76a8',
                    bi_icon='bi-linkedin').save()

        SocialMedia(name='GitHub',
                    base_url='https://github.com/',
                    icon_color='211F1F',
                    bi_icon='bi-github').save()

        SocialMedia(name='Twitter',
                    base_url='https://twitter.com/',
                    icon_color='00acee',
                    bi_icon='bi-twitter').save()

        SocialMedia(name='Facebook',
                    base_url='https://facebook.com/',
                    icon_color='39569c',
                    bi_icon='bi-facebook').save()

        SocialMedia(name='Instagram',
                    base_url='https://instagram.com/',
                    icon_color='3f729b',
                    bi_icon='bi-instagram').save()

        Skill(type=SkillType.SOFTWARE, name="MS Office").save()
        Skill(type=SkillType.SOFTWARE, name="LibreOffice").save()
        Skill(type=SkillType.SOFTWARE, name="Google Drive").save()
        Skill(type=SkillType.SOFTWARE, name="GIMP").save()
        Skill(type=SkillType.SOFTWARE, name="Trello").save()

        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="Python").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="Java").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="C").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="C++").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="C#").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="Matlab").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="R").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="JavaScript").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="HTML").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="CSS").save()
        Skill(type=SkillType.PROGRAMING_LANGUAGE, name="PHP").save()

        Skill(type=SkillType.PROGRAMING_TOOL, name="Git").save()
        Skill(type=SkillType.PROGRAMING_TOOL, name="Docker").save()
        Skill(type=SkillType.PROGRAMING_TOOL, name="virtualenv").save()
        Skill(type=SkillType.PROGRAMING_TOOL, name="Redis").save()
        Skill(type=SkillType.PROGRAMING_TOOL, name="Kafka").save()
        Skill(type=SkillType.PROGRAMING_TOOL, name="MongoDB").save()
        Skill(type=SkillType.PROGRAMING_TOOL, name="PostgreSQL").save()
        Skill(type=SkillType.PROGRAMING_TOOL, name="SQL Server").save()
        Skill(type=SkillType.PROGRAMING_TOOL, name="MySQL").save()

        Skill(type=SkillType.SOFTWARE_FRAMEWORK, name="Django").save()
        Skill(type=SkillType.SOFTWARE_FRAMEWORK, name="React").save()
        Skill(type=SkillType.SOFTWARE_FRAMEWORK, name="React Native").save()
        Skill(type=SkillType.SOFTWARE_FRAMEWORK, name="Expo").save()
        Skill(type=SkillType.SOFTWARE_FRAMEWORK, name="NodeJS").save()
        Skill(type=SkillType.SOFTWARE_FRAMEWORK, name=".NET Core").save()
        Skill(type=SkillType.SOFTWARE_FRAMEWORK, name="WordPress").save()
        Skill(type=SkillType.SOFTWARE_FRAMEWORK, name="Jakarta EE").save()
        Skill(type=SkillType.SOFTWARE_FRAMEWORK, name="Laravel").save()

        Skill(type=SkillType.ARCHITECTURE_PARADIGM, name="DevOps").save()
        Skill(type=SkillType.ARCHITECTURE_PARADIGM, name="Kanban").save()
        Skill(type=SkillType.ARCHITECTURE_PARADIGM, name="Scrum").save()
        Skill(type=SkillType.ARCHITECTURE_PARADIGM, name="Agile").save()
        Skill(type=SkillType.ARCHITECTURE_PARADIGM, name="CI/CD").save()

        Skill(type=SkillType.LANGUAGE, name="English", name_pt_br='Inglês').save()
        Skill(type=SkillType.LANGUAGE, name="Portuguese", name_pt_br='Português').save()
        Skill(type=SkillType.LANGUAGE, name="Spanish", name_pt_br='Espanhol').save()

        Skill(type=SkillType.SOFT_SKILL, name="Leadership", name_pt_br='Liderança').save()
        Skill(type=SkillType.SOFT_SKILL, name="Communication", name_pt_br="Comunicação").save()
        Skill(type=SkillType.SOFT_SKILL, name="Teamwork", name_pt_br="Trabalho em equipe").save()
        Skill(type=SkillType.SOFT_SKILL, name="Presentation", name_pt_br="Apresentação").save()
        Skill(type=SkillType.SOFT_SKILL, name="Problem solving", name_pt_br="Resolução de problemas").save()
        Skill(type=SkillType.SOFT_SKILL, name="Time management", name_pt_br="Gestão de tempo").save()

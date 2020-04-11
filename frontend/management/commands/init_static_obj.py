import glob
import os
from django.core.management.base import BaseCommand
from frontend.models import *

try:
    os.environ['LAB_TEST']
except:
    is_test = False
else:
    is_test = True

class Command(BaseCommand):
    help = 'Initializes the procedures'

    def is_absent(self, cls, name):

        try:
            a = cls.objects.get(name=name)
        except cls.DoesNotExist:
            return True
        else:
            return False

    def print(self, txt):
        if not is_test:
            print(txt)

    def handle(self, *args, **options):
        ###BasicStep creations

        ###Template:
        #name = "Geometrical Optimisation"
        #if self.is_absent(BasicStep, name):
        #    self.print("Adding BasicStep: {}".format(name))
        #    a = BasicStep.objects.create(name=name)

        name = "Geometrical Optimisation"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Optimizing geometry", error_message="Failed to optimize geometry", creates_ensemble=True, avail_xtb=True, avail_Gaussian=True, avail_orca=True)

        name = "Crest"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Finding conformers", error_message="Failed to find the conformers", creates_ensemble=True, avail_xtb=True)

        name = "Crest Pre NMR"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Finding conformers", error_message="Failed to find the conformers", creates_ensemble=True, avail_xtb=True)

        name = "Constrained Optimisation"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Optimizing geometry", error_message="Failed to optimize geometry", creates_ensemble=True, avail_xtb=True, avail_Gaussian=True, avail_orca=True)

        name = "Frequency Calculation"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Calculating frequencies", error_message="Failed to calculate frequencies", avail_xtb=True, avail_Gaussian=True, avail_orca=True)

        name = "TS Optimisation"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Optimizing the transition state", error_message="Failed to optimize the transition state", creates_ensemble=True, avail_xtb=True, avail_Gaussian=True, avail_orca=True)

        name = "UV-Vis Calculation"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Calculating UV-Vis spectrum", error_message="Failed to calculate the UV-Vis spectrum", avail_xtb=True, avail_Gaussian=True, avail_orca=True)

        '''
        name = "Enso"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Calculating NMR Spectrum", error_message="Failed to calculate the NMR spectrum")

        '''

        name = "Anmr"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Creating the final NMR Spectrum", error_message="Failed to create the final NMR spectrum", avail_xtb=True)

        name = "MO Calculation"
        if self.is_absent(BasicStep, name):
            self.print("Adding BasicStep: {}".format(name))
            a = BasicStep.objects.create(name=name, desc="Creating the Molecular Orbitals", error_message="Failed to create the Molecular Orbitals", avail_orca=True)



        ###Procedure creations

        ###Template:
        #name = "Simple Optimisation"
        #if self.is_absent(Procedure, name):
        #    self.print("Adding Procedure: {}".format(name))
        #    a = Procedure.objects.create(name=name)

        name = "Simple Optimisation"
        if self.is_absent(Procedure, name):
            self.print("Adding Procedure: {}".format(name))
            a = Procedure.objects.create(name=name)
            a.avail_xtb = True
            a.avail_Gaussian = True

            s_opt = BasicStep.objects.get(name="Geometrical Optimisation")
            step1 = Step.objects.create(step_model=s_opt, parent_procedure=a, from_procedure=a)
            step1.save()
            a.save()

        name = "Conformational Search"
        if self.is_absent(Procedure, name):
            self.print("Adding Procedure: {}".format(name))
            a = Procedure.objects.create(name=name)

            a.avail_xtb = True
            s_opt = BasicStep.objects.get(name="Crest")
            step1 = Step.objects.create(step_model=s_opt, parent_procedure=a, from_procedure=a)
            step1.save()
            a.save()

        name = "Constrained Optimisation"
        if self.is_absent(Procedure, name):
            self.print("Adding Procedure: {}".format(name))
            a = Procedure.objects.create(name=name)
            a.avail_xtb = True
            a.avail_Gaussian = True

            s_opt = BasicStep.objects.get(name="Constrained Optimisation")
            step1 = Step.objects.create(step_model=s_opt, parent_procedure=a, from_procedure=a)
            step1.save()
            a.save()

        name = "Opt+Freq"
        if self.is_absent(Procedure, name):
            self.print("Adding Procedure: {}".format(name))
            a = Procedure.objects.create(name=name)

            a.avail_xtb = True
            a.avail_Gaussian = True

            s_opt = BasicStep.objects.get(name="Geometrical Optimisation")
            step1 = Step.objects.create(step_model=s_opt, parent_procedure=a, from_procedure=a)
            step1.save()

            s_freq = BasicStep.objects.get(name="Frequency Calculation")
            step2 = Step.objects.create(step_model=s_freq, parent_step=step1, from_procedure=a)
            step2.save()

            a.save()

        name = "TS+Freq"
        if self.is_absent(Procedure, name):
            self.print("Adding Procedure: {}".format(name))
            a = Procedure.objects.create(name=name)

            a.avail_xtb = True
            a.avail_Gaussian = True

            s_opt = BasicStep.objects.get(name="TS Optimisation")
            step1 = Step.objects.create(step_model=s_opt, parent_procedure=a, from_procedure=a)
            step1.save()

            s_freq = BasicStep.objects.get(name="Frequency Calculation")
            step2 = Step.objects.create(step_model=s_freq, parent_step=step1, from_procedure=a)
            step2.save()

            a.save()

        name = "Simple UV-Vis"
        if self.is_absent(Procedure, name):
            self.print("Adding Procedure: {}".format(name))
            a = Procedure.objects.create(name=name)

            a.avail_xtb = True
            s_opt = BasicStep.objects.get(name="Geometrical Optimisation")
            step1 = Step.objects.create(step_model=s_opt, parent_procedure=a, from_procedure=a)
            step1.save()

            s_freq = BasicStep.objects.get(name="UV-Vis Calculation")
            step2 = Step.objects.create(step_model=s_freq, parent_step=step1, from_procedure=a)
            step2.save()

            a.save()

        name = "MO Generation"
        if self.is_absent(Procedure, name):
            self.print("Adding Procedure: {}".format(name))
            a = Procedure.objects.create(name=name)

            a.avail_orca = True

            s_opt = BasicStep.objects.get(name="Geometrical Optimisation")
            step1 = Step.objects.create(step_model=s_opt, parent_procedure=a, from_procedure=a)
            step1.save()

            s_freq = BasicStep.objects.get(name="MO Calculation")
            step2 = Step.objects.create(step_model=s_freq, parent_step=step1, from_procedure=a)
            step2.save()

            a.save()

        name = "NMR Prediction"
        if self.is_absent(Procedure, name):
            self.print("Adding Procedure: {}".format(name))
            a = Procedure.objects.create(name=name)

            a.avail_xtb = True

            s_crest = BasicStep.objects.get(name="Crest Pre NMR")
            step1 = Step.objects.create(step_model=s_crest, parent_procedure=a, from_procedure=a)
            step1.save()

            s_enso = BasicStep.objects.get(name="Enso")
            step2 = Step.objects.create(step_model=s_enso, parent_step=step1, from_procedure=a, same_dir=True)
            step2.save()

            s_anmr = BasicStep.objects.get(name="Anmr")
            step3 = Step.objects.create(step_model=s_anmr, parent_step=step2, from_procedure=a, same_dir=True)
            step3.save()

            a.save()

        ###Finishing the process
        self.verify()

    def verify(self):
        for proc in Procedure.objects.all():
            assert proc.initial_steps != None
            for step in proc.step_set.all():
                if step.step_model.name == "Frequency Calculation":
                    proc.has_freq = True
                elif step.step_model.name == "Anmr" or step.step_model.name == "Enso":
                    proc.has_nmr = True
                elif step.step_model.name == "UV-Vis Calculation":
                    proc.has_uvvis = True
                elif step.step_model.name == "MO Calculation":
                    proc.has_mo = True
        proc.save()

        for step in Step.objects.all():
            assert step.parent_step != None or step.parent_procedure != None

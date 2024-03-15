"""
ObjectOrientedProgramming1 3.0 A+
IntroductiontoComputerEngineering 3.0 A+
ObjectOrientedProgramming2 3.0 A0
CreativeComputerEngineeringDesign 3.0 A+
AssemblyLanguage 3.0 A+
InternetProgramming 3.0 B0
ApplicationProgramminginJava 3.0 A0
SystemProgramming 3.0 B0
OperatingSystem 3.0 B0
WirelessCommunicationsandNetworking 3.0 C+
LogicCircuits 3.0 B0
DataStructure 4.0 A+
MicroprocessorApplication 3.0 B+
EmbeddedSoftware 3.0 C0
ComputerSecurity 3.0 D+
Database 3.0 C+
Algorithm 3.0 B0
CapstoneDesigninCSE 2.0 B+
CompilerDesign 3.0 D0
ProblemSolving 4.0 P
"""

score_standard_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score_standard_dict = {}
for i in range(9):
    score_standard_dict[grade[i]] = score_standard_list[i]
# print(score_standard_dict)
# {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

total_score = 0
total_subject_score = 0
for _ in range(20):
    list_ = list(input().split())

    if list_[2] != 'P':
        total_subject_score += float(list_[1])
        # print(total_subject_score)
        total_score += (float(list_[1]) * score_standard_dict[list_[2]])
        # print(total_score)


average = round((total_score / total_subject_score), 6)
print(average)
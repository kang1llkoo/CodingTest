def solution(emergency):
    patients = {
        emerge: index + 1
        for index, emerge in enumerate(sorted(emergency, reverse=True))
    }
    return [patients[emerge] for emerge in emergency]
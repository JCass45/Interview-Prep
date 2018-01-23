def suspend(record: list):
    total_absences = 0
    consecutive_absences = 0

    for item in record:
        if item is True:
            total_absences += 1
            consecutive_absences += 1
            if consecutive_absences == 3 or total_absences == 7:
                return True

        else:
            consecutive_absences = 0

    return False


if __name__ == '__main__':
    absences = [True, False, True]
    print(suspend(absences))

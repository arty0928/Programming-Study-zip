#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int checkWrongDevice(int selectNum) {
    if (selectNum <= 0 || selectNum > 3) {
        return -1;
    }
    return 1;
}

int main() {
    int numStudents;
    printf("학생 수를 입력하세요: ");
    scanf("%d", &numStudents);

    int** submissions = (int**)malloc(numStudents * sizeof(int*));
    for (int i = 0; i < numStudents; i++) {
        submissions[i] = (int*)calloc(4, sizeof(int));
    }

    while (1) {
        int choice;
        printf("\n==== 메뉴 ====\n");
        printf("1번: 학생 제출\n");
        printf("2번: 교사 확인\n");
        printf("3번: 종료\n\n");
        printf("메뉴를 선택하세요: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1: {
            int studentNum, deviceNum;
            char submit;

            do {
                printf("\n\n학번 입력: ");
                scanf("%d", &studentNum);
            } while (studentNum <= 0 || studentNum > numStudents);

            printf("\n\n1번: 휴대폰, 2번: 컴퓨터, 3번: 태블릿\n");
            do {
                printf("제출할 전자기기를 선택하세요: ");
                scanf("%d", &deviceNum);
            } while (checkWrongDevice(deviceNum) != 1);

            printf("\n제출하시겠습니까?(Y/N): ");
            scanf(" %c", &submit);

            if (submit == 'Y' || submit == 'y') {
                submissions[studentNum - 1][deviceNum] = 1; // 학번을 인덱스로 활용하여 제출 정보 저장
                printf("(제출에 성공했습니다)\n");
            }
            else {
                printf("(제출에 실패했습니다)\n");
            }
            break;
        }
        case 2: {
            int checkNum = 0;
            printf("\n\n학번\t휴대폰\t컴퓨터\t태블릿\n");
            
            for (int studentNum = 1; studentNum <= numStudents; studentNum++) {
                printf("%d\t", studentNum);
                for (int deviceNum = 1; deviceNum <= 3; deviceNum++) {
                    int status = submissions[studentNum - 1][deviceNum];
                    if (status == 1) {
                        printf("\t  ■\t");
                    }
                    else {
                        printf("\t  □\t");
                    }
                }
                printf("\n");
            }
            do {
                printf("\n확인할 학번을 입력하세요: ");
                scanf("%d", &checkNum);
            } while (checkNum <= 0 || checkNum > numStudents);

            printf("\n\n학번\t휴대폰\t컴퓨터\t태블릿\n");
            printf("%d\t\t", checkNum);
            for (int deviceNum = 1; deviceNum <= 3; deviceNum++) {
                if (submissions[checkNum - 1][deviceNum] == 0)
                    printf("  □\t\t");
                else {
                     printf("  ■\t\t");
                }
            }
            printf("\n");
            break;
        }
        case 3: {
            printf("========== 프로그램을 종료합니다 ==========\n");
            for (int i = 0; i < numStudents; i++) {
                free(submissions[i]);
            }
            free(submissions);
            return 0;
        }
        default: {
            printf("잘못된 메뉴 선택입니다. 프로그램을 종료합니다.\n");
            for (int i = 0; i < numStudents; i++) {
                free(submissions[i]);
            }
            free(submissions);
            return 0;
        }
        }
    }

    return 0;
}


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decrypt_message(secret_message):

    first_word = secret_message[0][3]

    second_word = secret_message[1][9:13]

    third_word = secret_message[2][5:15:2]

    fourth_word = secret_message[3][7:13][::-1]

    fifth_word = secret_message[4][16:21][::-1]

    decrypted_message = f"{first_word} {second_word} {third_word} {fourth_word} {fifth_word}"
    return decrypted_message


def main():

    secret_message = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]

    decrypted_message = decrypt_message(secret_message)
    print("Расшифрованное сообщение:", decrypted_message)


if __name__ == "__main__":
    main()

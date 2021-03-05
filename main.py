alphabet = ['=', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
            'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
#cipher = 'ЦЁКРИКБРБНЩБУЭЧЯЬКСНКПУ=ОЪУРОПГГЛФАЗСЛЧЬСЧЛОРЗФШФНЧНЛ=НЮБХНЫ'
#key = 'ЗАКОН'
cipher='БЫЖХУНГОПКДРЯЪВМЙЩЛОЕСШЦЯЬХЕТЁП=ВЧЦЛРЦЖЮААУЫХХУНГОПКДЕЯЪВМЙЩЛ'
key='ПОБЕДА'
def getIds(string, alphabet):
    stringId = []
    t = 0
    for x in string:
        j = 0
        for a in alphabet:
            if string[t] == alphabet[j]:
                stringId.append(j)
            j += 1
        t += 1
    return stringId

def originalText(cipher_ids, key_ids, alphabet):
    plaintext = ''
    for i in range(len(cipher_ids)):
        value = (cipher_ids[i] - key_ids[i % len(key_ids)] + len(alphabet)) % len(alphabet)
        plaintext += alphabet[value]
    return plaintext


k_ids = getIds(key, alphabet)
c_ids = getIds(cipher, alphabet)
answer = originalText(c_ids, k_ids, alphabet)
print(answer)
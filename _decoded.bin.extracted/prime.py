import itertools
import sys


pub_key = "0x:cd:5f:8a:24:c7:60:50:08:89:7a:3c:92:2c:0e:81:2e:76:9d:e0:a4:64:42:c3:50:cb:78:c7:86:85:39:f3:d3:8a:ac:80:b3:e6:a5:06:60:59:10:e8:59:98:06:b4:d1:d1:48:f2:f6:b8:1d:a0:47:96:a8:a5:ae:e1:8f:29:e8:3e:16:77:5a:2a:0a:00:87:05:41:f6:57:4e:d1:43:86:36:ae:0a:0c:11:6e:07:10:4f:48:f7:20:94:86:3a:38:69:e1:c8:fc:22:06:27:27:89:62:fb:22:87:3e:31:56:f1:8e:55:de:c9:4e:97:00:64:ec:7f:4e:0e:88:45:40:12:e2:fd:5d:fe:5f:8d:19:bf:17:0f:9c:cb:3f:46:e0:fd:10:19:bc:b0:2d:90:83:a0:70:3c:61:7f:99:63:79:e6:47:83:54:a7:3a:e6:e6:ac:bc:e1:f4:33:3e:cf:af:24:36:6a:3e:97:7d:3c:d3:cb:fe:8d:8a:38:7b:d8:76:bf:da:b8:48:8f:6f:47:bf:1f:be:33:01:0f:d2:d7:e2:2b:4d:b2:e5:67:78:3c:e0:b6:06:db:86:b9:37:59:71:4c:4f:63:96:a7:fb:9f:74:c4:02:10:43:b0:f3:d4:6d:26:33:eb:d4:3a:87:78:63:df:7d:68:0f:50:65:87:c1:19:dd:64:10:0c:a8:31:ce:2a:f3:3d:95:1b:52:4c:5f:06:b4:9f:5b:f2:cb:38:1e:74:18:19:30:d0:6a:80:50:5c:06:ab:d5:bf:48:70:f0:c9:fb:58:1b:d8:0d:ba:88:96:60:63:9f:93:6e:de:a8:fe:5d:0c:9e:ae:58:06:2e:d6:93:25:25:83:c7:1c:c7:82:ba:61:3e:01:43:8e:69:b4:3f:9e:64:ec:a8:4f:9e:a0:4e:81:1a:d7:b3:9e:fd:78:76:d1:b6:b5:01:c4:f4:8a:cc:e6:f2:42:39:f6:c0:40:28:78:81:35:cd:88:c3:d1:5b:e0:f2:eb:b7:de:9e:9c:19:a7:a9:30:37:00:5e:e0:a9:a6:40:ba:da:33:2e:c0:d0:5e:e9:f0:8a:83:23:54:a0:48:7a:92:7d:5e:88:06:6e:25:69:e6:c5:d4:68:8e:42:2b:fa:0b:27:c6:17:1c:6d:7b:f0:29:bf:d9:16:57:52:af:19:aa:71:b3:3a:1e:a7:0b:6c:37:1f:b2:1e:47:f5:27:d8:0b:7d:04:f5:82:ad:9f:99:35:af:72:36:82:dc:01:ca:98:80:62:18:70:de:cb:7a:d1:56:48:cd:f4:ef:15:30:16:f3:e6:d8:79:33:b8:ec:54:cf:a1:fd:f8:7c:46:70:20:a3:e7:53"

prime1 = "0x:fb:40:dc:44:ba:03:d1:53:42:f7:59:08:e0:f9:30:05:96:64:4a:de:94:68:5e:08:e2:8c:9a:b1:64:0c:2f:62:c2:9a:b9:a2:39:82:4b:9e:be:eb:76:ae:6d:87:21:a3:5e:9e:d9:8d:7e:57:38:3e:59:09:34a5:78:cd:f7:2e:89:5d:5c:37:52:ea:fd:f6:31:cc:ba:d2:d9:60:e4:45:1d:67:76:d2:1f:12:9c:9d:c9:b1:90:45:51:ed:d2:fb:dd:b6:74:b4:99:fb:b1:0a:d9:b7:c2:be:8b:57:07:22:0a:8e:3a:36:ff:6d:c1:1d:63:93:af:cb:4e:c0:47:9f:65:bf:df:e3:f0:5f:1e:98:61:45:74:ec:36:a7:a5:b1:f1:8d:3d:97:6b:5a:82:49:09:00:08:0d:9d:c2:74:57:4e:30:a1:39:68:2f:22:34:71:13:aa:3b:f2:20:4f:8e:10:eb:d4:d0:9b:cd:8c:c2:53:5f:9d:71:13:0c:0f:21:b6:6e:13:39:40:d3:a6:b1:eb:74:ad:dd:0a:29:14:81:b1:90:ad:e0:53:f0:89:c8:00:fe:dc:ad:56:59:fc:28:1d:c0:cf:5e:08:c0:54:33:24:a3:52:bb:f3:25:10:43:c3:73:b8:40:4f:fc:6b:6b:77:bd:5f:22:24:eb:fb:15"
prime2 = "0xd140c9d7ad1f7e0b2d09c4c2dc2c2ad97d957ff8040556d729619d8bc9c53b287fa6efa132e45fce4caf56e9674776cd61746c8eb35aa821873dbfb592d94e0fcdaa3fabcf4134f32ca8a0837a3c3c7aab7e258006930edb636d0a82c7e8fe6098494ce2e3c96cab620c8b52f2b9cbdcabc1757c6b506bed5847e5877f95fca86ba25cba88106847aba5d011b33a29e374ba5598825e95aaad414f8ef67a0d8e012eb6f5bd13a976317c863b714ac971990309fc53a60bf7dbbe93f29174920e514aa334b77684e8e644a9328944db6f81d4c2e6c7f6afe0bc239b5a3aec7b13b9041f96e4fa0999fa030fc86a6c7bd0d551fa06fdbc4b291f51b58c2b9b26c7"
p = 31717798413454838971739311391870214101486054474438584033384974797696836002786889741922328038249283935148167589396475764515984792248325276562635675483085593307632384945480084324354199386711259069590701728377654610059849152461565385315663116675949927841648944186909571007960100266136674008112969369512988507367569334838093403144731951113528040013763615354283491955226704334394856253005551393545293491547587439064269735583121706098798182168292621767902095641352443871167789104818694502605762517497996162527138366803593402358312011933528177646501311411008602369245268966975849244259437732574655956250792264392115994984213
q = 26415754111957012456882978698568998595543408604540679602012008905307229528398419508696699258861541673208334031720118065722015191735056250991124159829757615035331104814626815428071461389740988358621575175288995137250131479702118666935818278843603742157096854979085966659730153703721295913600711482578441198179188796849780101926878867272222747848775311501107737838687624647749187764563156054858429897018261077616060929102880860789449995240869652963349913062375402021334173237153511868665597034141167420444312865576543827395764456254276820652449103574192677537410783040227047254038577626347718324544296319787177388746439
n = 837849563862443268467145186974119695264713699736869090645354954749227901572347301978135797019317859500555501198030540582269024532041297110543579716921121054608494680063992435808708593796476251796064060074170458193997424535149535571009862661106986816844991748325991752241516736019840401840150280563780565210071876568736454876944081872530701199426927496904961840225828224638335830986649773182889291953429581550269688392460126500500241969200245489815778699333733762961281550873031692933566002822719129034336264975002130651771127313980758562909726233111335221426610990708111420561543408517386750898610535272480495075060087676747037430993946235792405851007090987857400336566798760095401096997696558611588264303087788673650321049503980655866936279251406742641888332665054505305697841899685165810087938256696223326430000379461379116517951965921710056451210314300437093481577578273495492184643002539393573651797054497188546381723478952017972346925020598375000908655964982541016719356586602781209943943317644547996232516630476025321795055805235006790200867328602560320883328523659710885314500874028671969578391146701739515500370268679301080577468316159102141953941314919039404470348112690214065442074200255579004452618002777227561755664967507
e = 65537
d= 118370525227007068110186570733988041235576607807248896200395830233655814893241431084968175909819858417621242742154275832754457758856376855005920389993021649520424374669461616539555256877207891959957842626710778223266584582311511815493237688316364663276741056162936320460262194772536159431129765594092562266811961260813446384570933275214943656339074441824359395130246174404174000322037783998357751410604765179577140315024921971834715357627371911900213543145567250732540486740824273995939509286899864438850107228032176140268075557321022377191222594753770432201489100248201834734262026328066343082079358928359505377114924600461388021808147620175136768509457156427255160402062797794394199344781103672831290074439566751529983822098164980856581615999161891764310600269017166628918150345568093145105764852306653652447892885569706573841179397009260568259791565586868967165347947112010266100894829126306333574904005075277465193718571710380290644054431964779997554766021644649946133285410890067888020496324509852566219796399390364634306685384993869571442872586796766292465661785739009215588267511837697073523883029574481272539225104150953522658292050983386115413770734896974806099459808154373214219593317955386998794014437737295712013339975465
exp1 = 4492189219428533734160615962575939199078284902142895417823204236877214882858048286990906645879882409723443117090774494502912413471000430551511121043593702444137568046507257620865399372987074579000273028103230085151525395320937026511741230892261886113587523077694960680163657943913828953771222083522583568448140417870320322382614431088328230883436133447036931387283736967390223167682340174785043779674759397125204871838542131559409871170271634576646279990585980194579846780763952002276373463652843437761522473117032423832184141702656645023648094549902831182253300983436376896794423013469611922820999645972315190891305
exp2 = 3377695339399114460361007697850194672179894778614384165660018533446367448128213917067890501384862279650973330878962866636411299063731501034615872856147959381663406294865079470943724101591917274901945465445805869206037838166283998793386288305985921834634964138192782712186073333188648545950744804064991336813427561798696267057497976833563126584566536618692995454296081519571207004700234184349507034759189890144843227274396777597625630714229941740282165364034146649049855375243700954566393077896500953405302986305925466127172530683596132826762340173516252464462858566567017959150453644640338733229796956830745174751593
coeff = 5008766704441073110094275927475092934359438482494709413173835885956548796984235775999063952180035475135216886602837248432250571913557596676127722760043196879550414715509623720094870871267422874903674748355101055182611616540777474825294465818476764857357556425037827781523585362505433042323107128842789497183917141210209623467085568824693634496902808730858267370104547410231609050425903713097617823600441662256855554596415660476402731773770913509700338519064624973656573634030209544854864994564906296802423667202711122921059927602250312452090648723042264152542270684186773002652454231034276115004035074686109527525829
# d = 228405638158084920494285913460787379275819383851853200077359531585969844354968291150668693250333901122067299150159660009503309463195596596990579294482700592972448631368895263105701935345954876094244175004732126983138654298258718014429439954580426727951426256551139401561804744423203644488898801190092075062981179410663781423957246410830877224468315798791579168990887473082268267915774310744626481281969168744663335875968556134645111633721058961060430426445535522083024262292773250900541242868320670766492915571103258168696569317011123226615273115209347547869013410211856191702861185600177514355711772333864990341817547784691161100146430200567539646868700351730559589806123210749441011175303542936998401267600510860472810663202125642400083730296445158175292950048148425367668335842549509492458689674624064612104235349568051891112003569643956160769091057976660328698201095685128671705837613213765273968228958158379684914083072809785879459043742073177250241476053542015926031832215855946378319105599882431859769771136555439160519325257040764266754014365893564077137831378530561681827275283998004059732711030097050199878392998950694180192089249074519615945767417110653121080532043619951607578052375755305765059471673029597078104407216305
# exp1 = 3377695339399114460361007697850194672179894778614384165660018533446367448128213917067890501384862279650973330878962866636411299063731501034615872856147959381663406294865079470943724101591917274901945465445805869206037838166283998793386288305985921834634964138192782712186073333188648545950744804064991336813427561798696267057497976833563126584566536618692995454296081519571207004700234184349507034759189890144843227274396777597625630714229941740282165364034146649049855375243700954566393077896500953405302986305925466127172530683596132826762340173516252464462858566567017959150453644640338733229796956830745174751593
# exp2 = 12024264246349145024303430105454345688203665308854092152605651683203781916684763227063531326130604483068236283900270464006485978989705826851605496704978501060930998486084500355923386372415777911447827594307291400483472950513177008452809777976439580238573198064727730612354057395658669029205197808139512088917690902608627644193449699235739757416372813085100116794203594470607515277732474821068175950050232523338566488509102645356943195012329585664171958247995246479011265237581742578901295626233607516017969145150402773373850755494898330320362651749771415916706582793661824401510438995320271989408703204801433103014517
# coeff = 15739238195189026716238407609113992578495447841647712489844774216403657026182970865758292606339668009276004462392694652667189704256454933795330181460336884429130595932445447121005932034658953212997306657273318532778617543424203805469737487236667500602234014773893539547094805005127836285837139241116983791665041359905096038890615947428961788311155799480085019170904614347251219241445259980625960706692331992742223685378062599729064819954132000566296886624941423406199338596889931818295007243362907770271082999173902596386598313446120374140173358609278881438468970436124234056373338953790932134156714091348515741599915
# exp1 = d%(q-1)
# exp2 = d%(p-1)
# coeff = q^-1 (mod p)

# 7f -> fb : 4
# f4 -> 12 : 1
# 16 -> 54 : 1
# 04 -> 57 : 3
# b5 -> cd : 2

def remove_colon(string):
    string = string.replace(":", "")
    return string

# print("prime2: ", int(prime2, 16))
pub_key = remove_colon(pub_key)

pub_key = int(pub_key, 0)


combfb = [[1, 96, 102, 255], [1, 96, 102], [1, 96], [1],
          [96, 102, 255], [96, 102], [96], [96, 255],
          [1, 255], [1, 102],
          [102, 255], [102],
          [255],
          []]

comb12 = [[86], []]
comb54 = [[231], []]
comb57 = [[54, 110, 160], [54, 110], [54],
          [110, 160], [110],
          [160],
          [54, 160],  []]
combcd = [[62, 182], [62], [182], []]

reverse_char = {
    "fb": "7f",
    "12": "f4",
    "54": "16",
    "57": "a4",
    "cd": "b5"
}

def apply_changes(cont, comb, char):
    for i in comb:
        cont[i] = reverse_char[char]
    return cont

def list_as_string(l):
    return "".join(l)


char_list = ['fb', '12', '54', '57', 'cd']
pos_dict = {}
min_rem = pub_key

def find_prime1():
    with open("prime.txt", 'r') as f:
        content = f.read().split(":")
        # for each character
        for char in char_list:
            # find all its position in prime file
            pos_dict[char] = [i for i,val in enumerate(content) if val==char]
        print("Dictionary of position: ", pos_dict)

        res = []
        for c1 in combfb:
            for c2 in comb12:
                for c3 in comb54:
                    for c4 in comb57:
                        for c5 in combcd:
                            content_hex = content.copy()
                            content_hex = apply_changes(content_hex, c1, "fb")
                            content_hex = apply_changes(content_hex, c2, "12")
                            content_hex = apply_changes(content_hex, c3, "54")
                            content_hex = apply_changes(content_hex, c4, "57")
                            content_hex = apply_changes(content_hex, c5, "cd")
                            content_hex = list_as_string(content_hex)
                            # print(content_hex)
                            # print()
                            content_dec = int(content_hex, 0)
                            if pub_key%content_dec==0:#  and is_Prime(content_dec):
                                print("C1 : ", c1)
                                print("C2 : ", c2)
                                print("C3 : ", c3)
                                print("C4 : ", c4)
                                print("C5 : ", c5)
                                try:
                                    res.append(hex(pub_key/content_dec))

                                except:
                                    res.append("fail")
    print(res)
    return res


import random

def is_Prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False

    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True

    for i in range(8):#number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True



def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b

def find_d():
    phi = (p-1)*(q-1)
    d = mulinv(e, phi)
    return d


def find_coeff():
    coeff = mulinv(q, p)
    return coeff



if __name__ == "__main__":
    # 1 - find prime 2 'q'
    # p = find_prime1()
    # print(p)
    # 2 - find 'd' coeff (private key)
    # d = find_d()
    # print(d)
    # 3 - find exp1 & exp2
    # exp1 = d%(p-1)
    # exp2 = d%(q-1)
    # print("exp1: ", exp1)
    # print("exp2: ", exp2)
    # find coeff
    # q^-1 (mod p)
    # coeff = find_coeff()
    # print(coeff)
    print("p: ", hex(p))
    print()
    print("q: ", hex(q))
    print("p x q: ", p*q)
    print()
    print("n: ", hex(n))
    print()
    print("e: ", hex(e))
    print()
    print("d: ", hex(d))
    print()
    print("exp1: ", hex(exp1))
    print()
    print("exp2: ", hex(exp2))
    print("coeff: ", hex(coeff))
    assert p*q == n

#BU IPTAL BOTU BOTCU ANGARALI TARAFINDAN YAPILDI ISMILERI DEĞİŞTİRENE HARAM OLSUN
#BU IPTAL BOTUNUN ISIMLERI DEĞİŞTİRENİN ANASINI SİKEYİM
#2019 COPYRIGHT
from angarali.linepy import *
from angarali.akad.ttypes import *
from time import sleep
import time
import random


client = LINE("","")
anlikci1 = LINE("","")
anlikci2 = LINE("","")
anlikci3 = LINE("","")
new = LINE("","")
client.log("Auth Token : " + str(client.authToken))
client.log("Timeline Token : " + str(client.tl.channelAccessToken))
oepoll = OEPoll(client)

clientMID = client.getProfile().mid
IPTAL1 = new.getProfile().mid
IPTAL2 = anlikci1.getProfile().mid
IPTAL3 = anlikci2.getProfile().mid
IPTAL4 = anlikci3.getProfile().mid

amciklar = ["midleri burda eklernir.engelemek istediğniz kişiler"]

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        client.acceptGroupInvitation(op.param1)
        contact = client.getContact(op.param2)
        G = client.getGroup(op.param1)
        G.preventedJoinByTicket = False
        client.updateGroup(G)
        invsend = 0
        Ticket = client.reissueGroupTicket(op.param1)
        new.acceptGroupInvitationByTicket(op.param1,Ticket)
        anlikci1.acceptGroupInvitationByTicket(op.param1,Ticket)
        anlikci2.acceptGroupInvitationByTicket(op.param1,Ticket)
        anlikci3.acceptGroupInvitationByTicket(op.param1,Ticket)
        G = client.getGroup(op.param1)
        G.preventedJoinByTicket = True
        client.updateGroup(G)
        if G.invitee is None:
            client.sendMessage(op.param1, "LAN AMINI YARRAKLADIĞIM DAVET YOKSA BENIM NE İŞİM VAR BURDA HADI SIKTIR GIT BURDAN PUŞT " + client.getContact(op.param2).displayName)
            anlikci1.sendMessage(op.param1, "LAN AMINI YARRAKLADIĞIM DAVET YOKSA BENIM NE İŞİM VAR BURDA HADI SIKTIR GIT BURDAN PUŞT " + client.getContact(op.param2).displayName)
            anlikci2.sendMessage(op.param1, "LAN AMINI YARRAKLADIĞIM DAVET YOKSA BENIM NE İŞİM VAR BURDA HADI SIKTIR GIT BURDAN PUŞT " + client.getContact(op.param2).displayName)
            anlikci3.sendMessage(op.param1, "LAN AMINI YARRAKLADIĞIM DAVET YOKSA BENIM NE İŞİM VAR BURDA HADI SIKTIR GIT BURDAN PUŞT " + client.getContact(op.param2).displayName)
            new.sendMessage(op.param1, "LAN AMINI YARRAKLADIĞIM DAVET YOKSA BENIM NE İŞİM VAR BURDA HADI SIKTIR GIT BURDAN PUŞT " + client.getContact(op.param2).displayName)
            client.kickoutFromGroup(op.param1, [op.param2])
            anlikci1.leaveGroup(op.param1)
            anlikci2.leaveGroup(op.param1)
            anlikci3.leaveGroup(op.param1)
            new.leaveGroup(op.param1)
            client.leaveGroup(op.param1)
        else:
            if op.param2 in amciklar:
                client.sendMessage(op.param1, "LAN AMCIK {} SENIN GIBI EZIK BOTÇULARIN BU BOTU KULLANMA HAKKI YOKTUR".format(str(contact.displayName)))
                anlikci1.leaveGroup(op.param1)
                anlikci2.leaveGroup(op.param1)
                anlikci3.leaveGroup(op.param1)
                new.leaveGroup(op.param1)
                client.leaveGroup(op.param1)
            else:
                G = client.getGroup(op.param1)
                groupinvitingmembersmid = [contact.mid for contact in G.invitee]
                for _mid in groupinvitingmembersmid:
                    cancel = ([client, anlikci1, anlikci2, anlikci3, new])
                    random.choice(cancel).cancelGroupInvitation(op.param1, [_mid])
                    time.sleep(0.09)
            try:
                client.sendMessage(op.param1, "Succes canceled 「 {} 」user".format(str(len(groupinvitingmembersmid))))
                client.sendMessage(op.param1, "SUPPORTED BY: ANGARALI_06 "+ G.name)
                anlikci1.sendMessage(op.param1, "SUPPORTED BY: ANGARALI_06 "+ G.name)
                anlikci2.sendMessage(op.param1, "SUPPORTED BY: ANGARALI_06 "+ G.name)
                anlikci3.sendMessage(op.param1, "SUPPORTED BY: ANGARALI_06 "+ G.name)
                new.sendMessage(op.param1, "SUPPORTED BY: ANGARALI_06 "+ G.name)
                anlikci1.leaveGroup(op.param1)
                anlikci2.leaveGroup(op.param1)
                anlikci3.leaveGroup(op.param1)
                new.leaveGroup(op.param1)
                client.leaveGroup(op.param1)
            except:
                pass
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return


oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})


while True:
    oepoll.trace()
    

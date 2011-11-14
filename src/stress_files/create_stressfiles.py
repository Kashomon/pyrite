#!/usr/bin/python
# Copyright (c) 2011 by Joshua Hoak, Alissa Pajer 
# Licensed under the MIT License 
# Author: Josh Hoak (jrhoak@gmail.com)

text = """
The Merchant of Venice

Actus primus.

Enter Anthonio, Salarino, and Salanio.

  Anthonio. In sooth I know not why I am so sad,
It wearies me: you say it wearies you;
But how I caught it, found it, or came by it,
What stuffe 'tis made of, whereof it is borne,
I am to learne: and such a Want-wit sadnesse makes of
mee,
That I haue much ado to know my selfe

   Sal. Your minde is tossing on the Ocean,
There where your Argosies with portly saile
Like Signiors and rich Burgers on the flood,
Or as it were the Pageants of the sea,
Do ouer-peere the pettie Traffiquers
That curtsie to them, do them reuerence
As they flye by them with their wouen wings

   Salar. Beleeue me sir, had I such venture forth,
The better part of my affections, would
Be with my hopes abroad. I should be still
Plucking the grasse to know where sits the winde,
Peering in Maps for ports, and peers, and rodes:
And euery obiect that might make me feare
Misfortune to my ventures, out of doubt
Would make me sad

   Sal. My winde cooling my broth,
Would blow me to an Ague, when I thought
What harme a winde too great might doe at sea.
I should not see the sandie houre-glasse runne,
But I should thinke of shallows, and of flats,
And see my wealthy Andrew docks in sand,
Vailing her high top lower then her ribs
To kisse her buriall; should I goe to Church
And see the holy edifice of stone,
And not bethinke me straight of dangerous rocks,
Which touching but my gentle Vessels side
Would scatter all her spices on the streame,
Enrobe the roring waters with my silkes,
And in a word, but euen now worth this,
And now worth nothing. Shall I haue the thought
To thinke on this, and shall I lacke the thought
That such a thing bechaunc'd would make me sad?
But tell me, I know Anthonio
Is sad to thinke vpon his merchandize

   Anth. Beleeue me no, I thanke my fortune for it,
My ventures are not in one bottome trusted,
Nor to one place; nor is my whole estate
Vpon the fortune of this present yeere:
Therefore my merchandize makes me not sad
Sola. Why then you are in loue
"""

out_yaml = """
---
title: Post_%d
date: 13 November 2011
---
%s
"""

for i in range(10000):
    
    out = open("file_" + str(i) + ".yaml", "w")

    out.write(out_yaml % (i,text))

    out.close()


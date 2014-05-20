﻿#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import re
import string
import datetime
import getopt
import os
# print os.path.abspath(sys.argv[0]);
# dirname = ;
sys.path.append('/opt/mishkal/lib');
sys.path.append('../lib');
# join the actual dirctory to lib path
# print os.path.join(os.path.dirname(sys.argv[0]), 'lib');
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), 'lib'));
# sys.exit();
import pyarabic.araby as araby
import tashaphyne.stemming as stemmer
# all tashkeel and special chars
#symbols is a list
symbols=araby.TASHKEEL+araby.WEAK + (araby.TEH_MARBUTA, araby.ALEF_HAMZA_BELOW);

NON_TASHKEEL_pattern =re.compile(ur"[^"+u''.join(symbols)+u"]", re.UNICODE)
NON_VOCALIZATION_pattern =re.compile(ur"[^"+u''.join(araby.TASHKEEL)+u"]", re.UNICODE)

analyzer=stemmer.ArabicLightStemmer()

def extractHarakat(word, joker=araby.TATWEEL):
	"""
	Extract all harakats from the word, all other letters will be replaced with a joker
	"""
	harakatPattern = re.sub(NON_TASHKEEL_pattern,joker, word);
	return harakatPattern
def extractPattern(word, joker=araby.TATWEEL):
	"""
	Extract all harakats from the word, all other letters will be replaced with a joker
	"""
	starword, left, right= analyzer.transformToStars(word);
	# harakatPattern = re.sub(NON_TASHKEEL_pattern,joker, word);
	starword = re.sub(NON_TASHKEEL_pattern,joker, starword);
	#print newword.encode('utf8');
	# return newword;
	return starword

def extractVocalization(word, joker=''):
	"""
	Extract all harakats from the word, all other letters will be replaced with a joker
	"""
	harakatPattern = re.sub(NON_VOCALIZATION_pattern,joker, word);
	return harakatPattern
if __name__ == '__main__':
	text=u"""54:* حَدِيثٌ كم حم عم:  إِذَا كَانَ يَوْمُ الْقِيَامَةِ كُنْتُ إِمَامَ النَّبِيِّينَ وَخَطِيبَهُمْ وَصَاحِبَ شَفَاعَتِهِمْ، غَيْرَ فَخْرٍ  كم فِي الإِيمَانِ: ثنا الْحُسَيْنُ بْنُ الْحَسَنِ الطُّوسِيُّ، ثنا أَبُو حَاتِمٍ الرَّازِيُّ، ثنا عَبْدُ اللَّهِ بْنُ جَعْفَرٍ الرَّقِّيُّ، ثنا عُبَيْدُ اللَّهِ بْنُ عَمْرٍو وَعَنْ مُحَمَّدِ بْنِ صَالِحِ بْنِ هَانِئٍ، ثنا السَّرِيُّ بْنُ خُزَيْمَةَ، ثنا أَبُو حُذَيْفَةَ النَّهْدِيُّ، ثنا زُهَيْرُ بْنُ مُحَمَّدٍ، كِلاهُمَا عَنْ عَبْدِ اللَّهِ بْنِ مُحَمَّدِ بْنِ عَقِيلٍ، عَنِ الطُّفَيْلِ بْنِ أُبَيِّ بْنِ كَعْبٍ، عَنْ أَبِيهِ، بِهِ وَقَالَ: صَحِيحُ الإِسْنَادِ وَلَمْ يُخَرِّجَاهُ لِتَفَرُّدِ ابْنِ عَقِيلٍ بِهِ لِمَا نُسِبَ إِلَيْهِ مِنْ سُوءِ الْحِفْظِ، وَهُوَ عِنْدَ أَئِمَّتِنَا مِنَ الْمُتَقَدِّمِينَ ثِقَةٌ مَأْمُونٌ وَفِي الْفَضَائِلِ: أَنَا الْقَطِيعِيُّ، ثنا عَبْدُ اللَّهِ بْنُ أَحْمَدَ، حَدَّثَنِي أَبِي، ثنا عَبْدُ الرَّحْمَنِ، وَهُوَ ابْنُ مَهْدِيٍّ، ثنا زُهَيْرُ بْنُ مُحَمَّدٍ، عَنْ عَبْدِ اللَّهِ بْنِ مُحَمَّدٍ، بِهِ وَرَوَاهُ الإِمَامُ أَحْمَدُ: عَنْ أَبِي عَامِرٍ، عَنْ زُهَيْرٍ، يَعْنِي: ابْنَ مُحَمَّدٍ، عَنْ عَبْدِ اللَّهِ بْنِ مُحَمَّدٍ، بِهِ وَعَنْ زَكَرِيَّا بْنِ عَدِيٍّ، وَأَحْمَدَ بْنِ عَبْدِ الْمَلِكِ الْحَرَّانِيِّ، كِلاهُمَا عَنْ عُبَيْدِ اللَّهِ بْنِ عَمْرٍو، بِهِ وَعَنْ أَبِي أَحْمَدَ الزُّبَيْرِيِّ، عَنْ شَرِيكٍ، عَنْ عَبْدِ اللَّهِ بْنِ مُحَمَّدٍ، بِهِ وَرَوَاهُ ابْنُهُ عَبْدُ اللَّهِ فِي زِيَادَاتِهِ: حَدَّثَنِي عُبَيْدُ اللَّهِ الْقَوَارِيرِيُّ، ثنا مُحَمَّدُ بْنُ عَبْدِ اللَّهِ بْنِ الزُّبَيْرِ، ثنا شَرِيكٌ، بِهِ وَقَالَ أَيْضًا: ثنا هَاشِمُ بْنُ الْحَارِثِ، ثنا عُبَيْدُ اللَّهِ بْنُ عَمْرٍو، بِهِ وَحَدَّثَنِي(1/24)
56:* حَدِيثٌ كم حم: بَيْنَا نَحْنُ فِي صَلاةِ الظَّهِيرَةِ وَالنَّاسُ فِي الصُّفُوفِ فَرَأَيْنَاهُ يَتَنَاوَلُ شَيْئًا الْحَدِيثَ كم فِي الأَهْوَالِ: أنا عَبْدُ الرَّحْمَنِ بْنُ حَمْدَانَ، ثنا هِلالُ بْنُ الْعَلاءِ، ثنا أَبِي، ثنا عُبَيْدُ اللَّهِ بْنُ عَمْرٍو، عَنْ عَبْدِ اللَّهِ بْنِ مُحَمَّدِ بْنِ عَقِيلٍ، عَنِ الطُّفَيْلِ بْنِ أُبَيِّ بْنِ كَعْبٍ، عَنْ أَبِيهِ، وَقَالَ: صَحِيحُ الإِسْنَادِ رَوَاهُ أَحْمَدُ بِطُولِهِ: عَنْ أَحْمَدَ بْنِ عَبْدِ الْمَلِكِ بْنِ وَاقِدٍ الْحَرَّانِيِّ، عَنْ عُبَيْدِ اللَّهِ بْنِ عَمْرٍو، بِهِ قُلْتُ: رَوَاهُ زَكَرِيَّا بْنُ عَدِيٍّ، عَنْ عُبَيْدِ اللَّهِ بْنِ عَمْرٍو، فَقَالَ: عَنْ عَبْدِ اللَّهِ بْنِ مُحَمَّدِ بْنِ عَقِيلٍ، عَنْ جَابِرٍ وَأَخْرَجَهُ أَحْمَدُ، أَيْضًا: عَنْ زَكَرِيَّا.
68:* عَبْدُ اللَّهِ بْنُ رَبَاحٍ، عَنْ أُبَيٍّ حَدِيثٌ كم م حم عم: قَالَ لِي رَسُولُ اللَّهِ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم:  أَيُّ آيَةٍ فِي كِتَابِ اللَّهِ أَعْظَمُ؟  قَالَ: قُلْتُ: {اللَّهُ لا إِلَهَ إِلا هُوَ الْحَيُّ الْقَيُّومُ} قال: فَضَرَبَ صَدْرِي وَقَالَ:  لِيَهْنِكَ الْعِلْمُ أَبَا الْمُنْذِرِ  كم فِي الْمَعْرِفَةِ: ثنا أَبُو عَبْدِ اللَّهِ الْحَافِظُ، ثنا إِبْرَاهِيمُ بْنُ عَبْدِ اللَّهِ، ثنا يَزِيدُ بْنُ هَارُونَ، أَنَا الْجُرَيْرِيُّ، عَنْ أَبِي السَّلِيلِ، عَنْ عَبْدِ اللَّهِ بْنِ رَبَاحٍ، عَنْهُ، بِهَذَا قُلْتُ: هُوَ فِي مُسْلِمٍ، فَلا يُسْتَدْرَكُ وَرَوَاهُ الإِمَامُ أَحْمَدُ: ثنا عَبْدُ الرَّزَّاقِ، أَنَا سُفْيَانُ، عَنْ سَعِيدٍ الْجُرَيْرِيِّ، بِهِ وَرَوَاهُ ابْنُهُ عَبْدُ اللَّهِ، فِي زِيَادَاتِهِ: حَدَّثَنِي عُبَيْدُ اللَّهِ الْقَوَارِيرِيُّ، ثنا جَعْفَرُ بْنُ سُلَيْمَانَ، ثنا الْجُرَيْرِيُّ، عَنْ بَعْضِ أَصْحَابِهِ، عَنْ عَبْدِ اللَّهِ بْنِ رَبَاحٍ، بِهِ.
79:حَدِيثٌ كم حم: إِنِّي تَلَقَّيْتُ الْقُرْآنَ مِمَّنْ تَلَقَّاهُ مِنْ جِبْرِيلَ وَهُوَ رَطِبٌ الْحَدِيثَ، وَفِيهِ قِصَّةٌ لَهُ مَعَ عُمَرَ كم فِي أَوَّلِ التَّفْسِيرِ: ثنا عَلِيُّ بْنُ حَمْشَاذَ، ثنا مُحَمَّدُ بْنُ غَالِبٍ، ثنا عَفَّانُ بْنُ مُسْلِمٍ، وَأَبُو الْوَلِيدِ قَالا: ثنا أَبُو عَوَانَةَ، عَنِ الأَسْوَدِ بْنِ قَيْسٍ، عَنْ نُبَيْحٍ الْعَنْزِيِّ، عَنِ ابْنِ عَبَّاسٍ، فَذَكَرَ قِصَّةً فِيهَا هَذَا وَقَالَ: صَحِيحُ الإِسْنَادِ رَوَاهُ أَحْمَدُ: ثنا هِشَامُ بْنُ عَبْدِ الْمَلِكِ، وَعَفَّانُ، وَهُوَ لَفْظُهُ، قَالا: ثنا أَبُو عَوَانَةَ، بِهِ.(1/34)
84:حَدِيثٌ جا حب قط عم كم: كَانَ رَسُولُ اللَّهِ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم، يُوتِرُ بِثَلاثِ رَكَعَاتٍ الْحَدِيثَ جا فِي الصَّلاةِ: ثنا إِبْرَاهِيمُ بْنُ أَبِي بَكْرِ بْنِ أَبِي شَيْبَةَ، ثنا مُحَمَّدُ بْنُ أَبِي عُبَيْدَةَ بْنِ مَعْنٍ، عَنْ أَبِيهِ، عَنِ الأَعْمَشِ، عَنْ طَلْحَةَ الْيَامِيِّ، عَنْ ذَرٍّ، عَنْ سَعِيدِ بْنِ عَبْدِ الرَّحْمَنِ بْنِ أَبْزَى، عَنْ أَبِيهِ، عَنْهُ، بِهِ حب فِي الرَّابِعِ وَالثَّلاثِينَ مِنَ الْخَامِسِ: أَنَا أَحْمَدُ بْنُ الْحَسَنِ بْنِ عَبْدِ الْجَبَّارِ، ثنا يَحْيَى بْنُ مَعِينٍ، ثنا أَبُو حَفْصٍ الأَبَّارُ، عَنِ الأَعْمَشِ، عَنْ زُبَيْدٍ، وَطَلْحَةَ الْيَامِيِّ، عَنْ ذَرٍّ، بِهِ وَعَنْ أَبِي يَعْلَى، ثنا مُحَمَّدُ بْنُ عَبْدِ اللَّهِ بْنِ نُمَيْرٍ، ثنا مُحَمَّدُ بْنُ أَبِي عُبَيْدَةَ، بِهِ قط فِي الصَّلاةِ: ثنا الْحُسَيْنُ بْنُ إِسْمَاعِيلَ، ثنا يُوسُفُ بْنُ مُوسَى، ثنا عَبْدُ الرَّحْمَنِ بْنِ عَبْدِ اللَّهِ الدَّشْتَكِيُّ، عَنْ أَبِي جَعْفَرٍ الرَّازِيُّ، عَنِ الأَعْمَشِ، بِهِ وَعَنْ عَبْدِ اللَّهِ بْنِ سُلَيْمَانَ، ثَنَا الْمُسَيَّبُ بْنُ وَاضِحٍ، نا عِيسَى بْنُ يُونُسَ، عَنْ سَعِيدِ بْنِ أَبِي عَرُوبَةَ، عَنْ قَتَادَةَ، عَنْ عَزْرَةَ، عَنْ سَعِيدِ بْنِ عَبْدِ الرَّحْمَنِ، بِهِ، وَفِيهِ أَلْفَاظٌ تَفَرَّدَ بِهَا وَقَالَ عَبْدُ اللَّهِ: وَرُبَّمَا لَمْ يَقُلِ الْمُسَيَّبُ: عَنْ عَزْرَةَ كم فِي آخِرِ الْقِرَاءَاتِ: ثَنَا أَبُو بَكْرِ بْنُ إِسْحَاقَ، ثَنَا الْحَسَنُ بْنُ عَلِيِّ بْنِ زِيَادٍ، ثنا إِبْرَاهِيمُ بْنُ مُوسَى، ثَنَا أَبُو أَنَسٍ مُحَمَّدُ بْنُ أَنَسٍ، ثنا الأَعْمَشُ، بِهِ رَوَاهُ عَبْدُ اللَّهِ بْنُ أَحْمَدَ: عَنْ أَبِي بَكْرِ بْنِ أَبِي شَيْبَةَ، عَنْ مُحَمَّدِ بْنِ أَبِي عُبَيْدَةَ، بِهِ وَعَنْ عُثْمَانَ بْنِ أَبِي شَيْبَةَ،(1/37)
87:* حَدِيثٌ كم عم: لا تَسُبُّوا الرِّيحَ، فَإِنَّهَا مِنْ نَفْسِ الرَّحْمَنِ، قَوْلُهُ: {وَتَصْرِيفِ الرِّيَاحِ} الآية، وَلَكِنْ قُولُوا: اللَّهُمَّ إِنَّا نَسْأَلُكَ مِنْ خَيْرِ هَذِهِ الرِّيحِ الْحَدِيثَ كم فِي تَفْسِيرِ الْبَقَرَةِ: أَنَا يَحْيَى بْنُ مُحَمَّدٍ الْعَنْبَرِيُّ، ثنا مُحَمَّدُ بْنُ عَبْدِ السَّلامِ، ثنا إِسْحَاقُ بْنُ إِبْرَاهِيمَ، أَنَا جَرِيرٌ، عَنِ الأَعْمَشِ، عَنْ حَبِيبِ بْنِ أَبِي ثَابِتٍ، عَنْ ذَرٍّ، عَنْ سَعِيدِ بْنِ عَبْدِ الرَّحْمَنِ، بْنِ أَبْزَى أَظُنُّهُ عَنْ أَبِيهِ، عَنْ أُبَيٍّ، بِهِ قَوْلُهُ، وَقَالَ: صَحِيحٌ عَلَى شَرْطِهِمَا، وَقَدْ أُسْنِدَ مِنْ حَدِيثِ حَبِيبٍ وَرَوَاهُ عَبْدُ اللَّهِ بْنُ أَحْمَدَ فِي زِيَادَاتِهِ: حَدَّثَنِي أَبُو مُوسَى مُحَمَّدُ بْنُ الْمُثَنَّى، ثنا أَسْبَاطُ بْنُ مُحَمَّدٍ الْقُرَشِيُّ، ثنا الأَعْمَشُ، بِهِ، لَيْسَ فِيهِ: عَنْ ذَرٍّ وَعَنْ مُحَمَّدِ بْنِ يَزِيدَ الْكُوفِيِّ، عَنِ ابْنِ فُضَيْلٍ، عَنِ الأَعْمَشِ، مِثْلَ الأَوَّلِ.(1/39)
112:* أَبُو رَافِعٍ الصَّائِغُ، عَنْ أُبَيٍّ، حَدِيثٌ خز عه حب كم حم عم: أَنَّ رَسُولَ اللَّهِ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم، كَانَ يَعْتَكِفُ، فَلَمْ يَعْتَكِفْ عَامًا، فَاعْتَكَفَ مِنَ الْعَامِ الْمُقْبِلِ عِشْرِينَ لَيْلَةً خز فِي الصِّيَامِ: ثنا عَبْدُ الْوَارِثِ بْنُ عَبْدِ الصَّمَدِ بْنِ عَبْدِ الْوَارِثِ، ثنا أَبِي، ثَنَا حَمَّادٌ، عَنْ ثَابِتٍ، عَنْ أَبِي رَافِعٍ، عَنْهُ بِهَذَا عه فِيهِ: عَنْ يُوسُفَ الْقَاضِي، عَنْ مُحَمَّدِ بْنِ أَبِي بَكْرٍ الْمُقَدِّمِيِّ، عَنْ بَهْزِ بْنِ أَسَدٍ، عَنْ حَمَّادِ بْنِ سَلَمَةَ قَالَ أَبُو عَوَانَةَ: لَمْ يُخَرِّجْهُ مُسْلِمٌ، وَفِي صِحَّتِهِ نَظَرٌ حب فِي الثَّامِنِ مِنَ الْخَامِسِ: أَنَا أَحْمَدُ بْنُ عَلِيِّ بْنِ الْمُثَنَّى، ثنا هُدْبَةُ، ثَنا حَمَّادٌ، بِهِ كم فِي الصِّيَامِ: ثنا أَبُو النَّضْرِ الْفَقِيهُ، ثنا عُثْمَانُ بْنُ سَعِيدٍ، ثنا سَهْلُ بْنُ بَكَّارٍ، وَمُوسَى بْنُ إِسْمَاعِيلَ، قَالا: ثنا حَمَّادٌ، بِهِ رَوَاهُ أَحْمَدُ: عَنْ عَبْدِ الرَّحْمَنِ بْنِ مَهْدِيٍّ، وَحَسَنِ بْنِ مُوسَى، وَعَفَّانَ، ثَلاثَتُهُمْ عَنْ حَمَّادٍ، بِهِ وَرَوَاهُ عَبْدُ اللَّهِ بْنُ أَحْمَدَ فِي زِيَادَاتِهِ: عَنْ هُدْبَةَ، بِهِ.(1/51)
121:* حَدِيثٌ عه حب كم طح حم: بَعَثَنَا رَسُولُ اللَّهِ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم، فَصَبَّحْنَا الْحُرَقَاتِ مِنْ جُهَيْنَةَ الْحَدِيثَ عه فِي الإِيمَانِ: ثنا الصَّغَانِيُّ، وَأَبُو أُمَيَّةَ، وَأَبُو عُبَيْدَةَ السَّرِيُّ بْنُ يَحْيَى، قَالُوا: ثنا يَعْلَى بْنُ عُبَيْدٍ وَعَنْ مُحَمَّدِ بْنِ عَبْدِ الْمَلِكِ الْوَاسِطِيِّ، وَمُحَمَّدِ بْنِ إِسْرَائِيلَ الْجَوْهَرِيِّ، وَمُحَمَّدِ بْنِ إِسْحَاقَ الْخَيَّاطِ، قَالُوا: ثنا أَبَوُ مَنْصُورٍ الْحَارِثُ بْنُ مَنْصُورٍ، ثنا سُفْيَانُ الثَّوْرِيُّ، كِلاهُمَا، عَنِ الأَعْمَشِ، عَنْ أَبِي ظَبْيَانَ، عَنْهُ، بِهِ وَفِيهِ قِصَّةُ سَعْدِ بْنِ أَبِي وَقَّاصٍ وَعَنِ الصَّغَانِيِّ، أَنَا خَلَفُ بْنُ سَالِمٍ، ثنا هُشَيْمٌ عَنِ الدَّنْدَانِيِّ، ثنا أَبُو الْوَلِيدِ، ثَنَا أَبُو عَوَانَةَ وَعَنْ أَبِي أُمَيَّةَ، ثَنَا مُحَمَّدُ بْنُ الصَّلْتِ، عَنْ أَبِي كُدَيْنَةَ، ثَلاثَتُهُمْ عَنْ حُصَيْنٍ، ثنا أَبُو ظَبْيَانَ، بِهِ حب فِي التَّاسِعِ وَالسِّتِّينَ مِنَ الثَّانِي: أنا أَبُو يَعْلَى: ثنا سُرَيْجُ بْنُ يُونُسَ، ثنا هُشَيْمٌ، أنا حُصَيْنٌ، ثنا أَبُو ظَبْيَانَ، سَمِعْتُ أُسَامَةَ، بِهِ كم فِي مَنَاقِبِ عَلِيٍّ: ثنا أَبُو عَبْدِ اللَّهِ مُحَمَّدُ بْنُ يَعْقُوبَ الشَّيْبَانِيُّ، ثنا حَامِدُ بْنُ أَبِي حَامِدٍ، ثنا عَبْدُ الرَّحْمَنِ بْنُ عَبْدِ اللَّهِ بْنِ سَعْدٍ الدَّشْتَكِيُّ، ثنا عَمْرُو بْنُ أَبِي قَيْسٍ، عَنْ إِبْرَاهِيمَ بْنِ مُهَاجِرٍ، عَنْ أَبِي الشَّعْثَاءِ، عَنْ عَمِّهِ، عَنْ أُسَامَةَ، بِهِ قَالَ: وَثَنَاهُ أَبُو أَحْمَدَ الْقَاضِي، ثنا أَحْمَدُ بْنُ نَصْرٍ، ثنا(1/56)
123:* حَدِيثٌ مي خز حم: أَنَّ رَسُولَ اللَّهِ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم، كَانَ يَصُومُ يَوْمَ الاثْنَيْنِ وَالْخَمِيسِ الْحَدِيثَ، وَفِيهِ قِصَّةٌ مي في الصوم: أنا وَهْبُ بْنُ جَرِيرٍ، ثنا هِشَامٌ، عَنْ يَحْيَى، عَنْ عُمَرَ بْنِ الْحَكَمِ بْنِ ثَوْبَانَ، أَنَّ مَوْلَى قُدَامَةَ بْنِ مَظْعُونٍ حَدَّثَهُ، أَنَّ مَوْلَى أُسَامَةَ بْنِ زَيْدٍ حَدَّثَهُ، عَنْهُ، بِهِ خز فِيهِ: عَنْ سَعِيدِ بْنِ أَبِي زَيْدُونٍ وَرَّاقِ الْفِرْيَابِيِّ، عَنْ مُحَمَّدِ بْنِ يُوسُفَ، عَنْ أَبِي بَكْرِ بْنِ عَيَّاشٍ، عَنْ عُمَرَ بْنِ مُحَمَّدٍ، عَنْ شُرَحْبِيلَ بْنِ سَعْدٍ، عَنْ أُسَامَةَ، نَحْوَهُ رَوَاهُ أَحْمَدُ: عَنْ زَيْدِ بْنِ الْحُبَابِ، أَخْبَرَنِي ثَابِتُ بْنُ قَيْسٍ أَبُو غُصْنٍ، حَدَّثَنِي أَبُو سَعِيدٍ الْمَقْبُرِيُّ، عَنْهُ، بِهِ وَعَنْ عَبْدِ الرَّحْمَنِ بْنِ مَهْدِيٍّ، ثنا ثَابِتُ بْنُ قَيْسٍ، وَفِيهِ زِيَادَةٌ فِي أَوَّلِهِ وَعَنْ عَفَّانَ، ثَنا أَبَانٌ، ثنا يَحْيَى بْنُ أَبِي كَثِيرٍ، حَدَّثَنِي عُمَرُ بْنُ الْحَكَمِ عَنْ مَوْلَى قُدَامَةَ بْنِ مَظْعُونٍ، عَنْ مَوْلَى أُسَامَةَ وَعَنْ إِسْمَاعِيلَ، عَنْ هِشَامٍ، عَنْ يَحْيَى، نَحْوَهُ.(1/57)
132:وَابْنُ عَبَّاسٍ يَأْمُرُ بِهِ؟ فَقَالَ: لَقَدْ لَقِيتُ ابْنَ عَبَّاسٍ، فَذَكَرَ الْقِصَّةَ، قَالَ: وَلَكِنَّ أُسَامَةَ بْنَ زَيْدٍ حَدَّثَنِي، فَذَكَرَهُ بِلَفْظِ:  لا رِبَا إِلا فِي الدَّيْنِ  حب فِي الْحَادِي وَالثَّمَانِينَ مِنَ الثَّانِي: ثنا مُحَمَّدُ بْنُ الْمُعَافَى بِصَيْدَا، ثنا مُحَمَّدُ بْنُ هِشَامِ بْنِ أَبِي خَيْرَةَ، ثنا عَبْدُ الرَّحْمَنِ بْنُ عُثْمَانَ الْبَكْرَاوِيُّ، ثنا عُثْمَانُ بْنُ الأَسْوَدِ، عَنِ ابْنِ أَبِي مُلَيْكَةَ، قَالَ: قَالَ ابْنُ عَبَّاسٍ لابْنِ عُمَرَ: أَتَتَّهِمُ أُسَامَةَ؟ قَالَ: لا قَالَ: فَإِنَّهُ أَخْبَرَنِي، فَذَكَرَهُ رَوَاهُ أَحْمَدُ: ثنا يَحْيَى بْنُ إِسْحَاقَ، وَعَفَّانُ قَالا: ثنا وُهَيْبٌ، ثنا عَبْدُ اللَّهِ بْنُ طَاوُسٍ، عَنْ أَبِيهِ، عَنِ ابْنِ عَبَّاسٍ، بِهِ وَعَنْ سُفْيَانَ، عَنْ عَمْرٍو، عَنْ أَبِي صَالِحٍ، سَمِعْتُ أَبَا سَعِيدٍ الْخُدْرِيَّ يَقُولُ: الذَّهَبُ بِالذَّهَبِ وَزْنًا بِوَزْنٍ، قَالَ: فَلَقِيتُ ابْنَ عَبَّاسٍ فَقُلْتُ: أَرَأَيْتَ مَا تَقُولُ؟ أَوَجَدْتَهُ فِي كِتَابِ اللَّهِ؟ فَذَكَرَ الْقِصَّةَ، قَالَ: لا، وَلَكِنْ أَخْبَرَنِي أُسَامَةُ، بِهِ وَعَنْ مُحَمَّدِ بْنِ جَعْفَرٍ، عَنْ شُعْبَةَ، عَنْ عَمْرٍو، عَنْ ذَكْوَانَ، وَهُوَ أَبُو صَالِحٍ، قَالَ: أَرَسْلَنِي أَبُو سَعِيدٍ الْخُدْرِيُّ إِلَى ابْنِ عَبَّاسٍ، فَذَكَرَهُ وَعَنْ مُحَمَّدِ بْنِ بَكْرٍ، عَنْ يَحْيَى بْنِ قَيْسٍ، عَنْ عَطَاءٍ، بِهِ وَعَنْ سُفْيَانَ، عَنْ عُبَيْدِ اللَّهِ بْنِ أَبِي يَزِيدَ، بِهِ، وَعَنْ عَبْدِ الصَّمَدِ، عَنْ دَاوُدَ بْنِ أَبِي الْفُرَاتِ، عَنْ إِبْرَاهِيمَ، يَعْنِي: الصَّائِغَ، عَنْ عَطَاءٍ، بِهِ وَعَنْ إِسْمَاعِيلَ، عَنْ خَالِدٍ الْحَذَّاءِ، عَنْ عِكْرِمَةَ، عَنِ ابْنِ عَبَّاسٍ، بِهِ وَعَنْ يَعْقُوبَ، ثنا أَبِي، عَنِ ابْنِ(1/65)
135:* عَبْدُ الرَّحْمَنِ بْنُ أَبِي لَيْلَى، عَنْ أُسَامَةَ حَدِيثٌ الطبراني: فِي قَوْلِهِ: {فَمِنْهُمْ ظَالِمٌ لِنَفْسِهِ وَمِنْهُمْ مُقْتَصِدٌ وَمِنْهُمْ سَابِقٌ بِالْخَيْرَاتِ} قَالَ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم:  وَكُلُّهُمْ مِنْ هَذِهِ الأُمَّةِ  قَالَ الطَّبَرَانِيُّ: حَدَّثَنَا عَبْدُ اللَّهِ بْنُ أَحْمَدَ بْنِ مُحَمَّدِ بْنِ الْعَبَّاسِ، ثنا أَبُو مَسْعُودٍ، حَدَّثَنَا سَهْلُ بْنُ عَبْدِ رَبِّهِ الرَّازِيُّ، عَنْ عَمْرِو بْنِ أَبِي قَيْسٍ، عَنِ ابْنِ أَبِي لَيْلَى، عَنْ عَبْدِ الرَّحْمَنِ، عَنْهُ، بِهِ.(1/66)
144:حَدِيثٌ عه حب كم:  قُمْتُ عَلَى بَابِ الْجَنَّةِ، فَإِذَا عَامَّةُ مَنْ دَخَلَهَا الْمَسَاكِينُ، وَإِذَا أَصْحَابُ الْجَدِّ مَحْبُوسُونَ، وَأَصْحَابُ النَّارِ قَدْ أُمِرَ بِهِمْ إِلَى النَّارِ، وَنَظَرْتُ إِلَى النَّارِ فَإِذَا عَامَّةُ مَنْ دَخَلَهَا النِّسَاءُ  عه فِي الْمَنَاقِبِ: ثنا مُحَمَّدُ بْنُ عَبْدِ الْمَلِكِ الْوَاسِطِيُّ، ثنا يَزِيدُ بْنُ هَارُونَ وَعَنِ الصَّغَانِيِّ، وَأَبِي أُمَيَّةَ، قَالا: ثنا هَوْذَةُ كِلاهُمَا، عَنْ سُلَيْمَانَ التَّيْمِيِّ، عَنْ أَبِي عُثْمَانَ، عَنْهُ، بِهِ حب فِي الْخَامِسِ وَالْخَمْسِينَ مِنَ الثَّانِي: أَنَا عِمْرَانُ بْنُ مُوسَى، ثنا عُبَيْدُ اللَّهِ بْنُ مُعَاذٍ، ثنا مُعْتَمِرُ بْنُ سُلَيْمَانَ، ثنا أَبِي، عَنْ أَبِي عُثْمَانَ النَّهْدِيِّ، عَنْ أُسَامَةَ بْنِ زَيْدٍ، بِهِ قَالَ ابْنُ حِبَّانَ: قَرَنَ عِمْرَانُ بْنُ مُوسَى بِأُسَامَةَ سَعِيدَ بْنَ زَيْدٍ، وَأَنَا أَهَابُهُ، وَقَدْ تَفَرَّدَ بِذَلِكَ مُعْتَمِرٌ وَفِي الثَّانِي مِنَ الثَّالِثِ: أَنَا مُحَمَّدُ بْنُ عَلِيٍّ الصَّيْرَفِيُّ غُلامُ طَالُوتَ، ثنا هُدْبَةُ بْنُ خَالِدٍ، ثنا حَمَّادُ بْنُ سَلَمَةَ، عَنِ التَّيْمِيِّ، نَحْوَهُ وَأَعَادَهُ فِي الثَّامِنِ وَالسَّبْعِينَ مِنَ الثَّالِثِ: عَنْ عِمْرَانَ بْنِ مُوسَى، بِهِ رَوَاهُ أَحْمَدُ: عَنْ إِسْمَاعِيلَ، وَيَحْيَى كِلاهُمَا: عَنِ التَّيْمِيِّ، بِهِ.
152:* حَدِيثٌ طح حم الطبراني: كَانَ رَسُولُ اللَّهِ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم، يُصَلِّي الظُّهْرَ بِالْهَجِيرِ طح فِي الصَّلاةِ: ثنا أَبُو بَكْرٍ، ثنا أَبُو دَاوُدَ، ثنا ابْنُ أَبِي ذِئْبٍ، عَنِ الزِّبْرِقَانِ، عَنْ عُرْوَةَ، عَنْهُ بِهَذَا رَوَاهُ أَحْمَدُ: ثنا يَزِيدُ، أنا ابْنُ أَبِي ذِئْبٍ، عَنِ الزِّبْرِقَانِ أَنَّ رَهْطًا مِنْ قُرَيْشٍ مَرَّ بِهِمْ زَيْدُ بْنُ ثَابِتٍ وَهُمْ مُجْتَمِعُونَ، فَأَرْسَلُوا إِلَيْهِ غُلامَيْنِ لَهُمْ يَسْأَلانِهِ عَنِ الصَّلاةِ الْوُسْطَى، فَقَالَ: هِيَ الْعَصْرُ، فَقَامَ إِلَيْهِ رَجُلانِ مِنْهُمْ فَسَأَلاهُ، فَقَالَ: هِيَ الظُّهْرُ، ثُمَّ انْصَرَفَ إِلَى أُسَامَةَ بْنِ زَيْدٍ، فَسَأَلاهُ، فَقَالَ: هِيَ الظُّهْرُ، ثُمَّ ذَكَرَ بَقِيَّةَ الْحَدِيثِ وَقَدْ رَوَاهُ الطَّبَرَانِيُّ: حَدَّثَنَا الأُسْفَاطِيُّ، ثَنا خَالِدُ بْنُ يَزِيدَ الْعُمَرِيُّ، عَنِ ابْنِ أَبِي ذِئْبٍ، عَنِ الزِّبْرِقَانِ، عَنْ زُهْرَةَ، عَنْ أُسَامَةَ: أَنَّ رَسُولَ اللَّهِ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم، صَلَّى الظُّهْرَ بِهَجِيرٍ.
154:كَانَ رَسُولُ اللَّهِ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم، يُصَلِّي الظُّهْرَ بِالْهَجِيرِ طح فِي الصَّلاةِ: ثنا أَبُو بَكْرٍ، ثنا أَبُو دَاوُدَ، ثنا ابْنُ أَبِي ذِئْبٍ، عَنِ الزِّبْرِقَانِ، عَنْ عُرْوَةَ، عَنْهُ بِهَذَا رَوَاهُ أَحْمَدُ: ثنا يَزِيدُ، أنا ابْنُ أَبِي ذِئْبٍ، عَنِ الزِّبْرِقَانِ أَنَّ رَهْطًا مِنْ قُرَيْشٍ مَرَّ بِهِمْ زَيْدُ بْنُ ثَابِتٍ وَهُمْ مُجْتَمِعُونَ، فَأَرْسَلُوا إِلَيْهِ غُلامَيْنِ لَهُمْ يَسْأَلانِهِ عَنِ الصَّلاةِ الْوُسْطَى، فَقَالَ: هِيَ الْعَصْرُ، فَقَامَ إِلَيْهِ رَجُلانِ مِنْهُمْ فَسَأَلاهُ، فَقَالَ: هِيَ الظُّهْرُ، ثُمَّ انْصَرَفَ إِلَى أُسَامَةَ بْنِ زَيْدٍ، فَسَأَلاهُ، فَقَالَ: هِيَ الظُّهْرُ، ثُمَّ ذَكَرَ بَقِيَّةَ الْحَدِيثِ وَقَدْ رَوَاهُ الطَّبَرَانِيُّ: حَدَّثَنَا الأُسْفَاطِيُّ، ثَنا خَالِدُ بْنُ يَزِيدَ الْعُمَرِيُّ، عَنِ ابْنِ أَبِي ذِئْبٍ، عَنِ الزِّبْرِقَانِ، عَنْ زُهْرَةَ، عَنْ أُسَامَةَ: -
157:كَانَ رَسُولُ اللَّهِ، صَلَّى اللَّهُ عَلِيهِ وَسَلَّم، يُصَلِّي الظُّهْرَ بِالْهَجِيرِ طح فِي الصَّلاةِ: ثنا أَبُو بَكْرٍ، ثنا أَبُو دَاوُدَ، ثنا ابْنُ أَبِي ذِئْبٍ، عَنِ الزِّبْرِقَانِ، عَنْ عُرْوَةَ، عَنْهُ بِهَذَا رَوَاهُ أَحْمَدُ: ثنا يَزِيدُ، أنا ابْنُ أَبِي ذِئْبٍ، عَنِ الزِّبْرِقَانِ أَنَّ رَهْطًا مِنْ قُرَيْشٍ مَرَّ بِهِمْ زَيْدُ بْنُ ثَابِتٍ وَهُمْ مُجْتَمِعُونَ، فَأَرْسَلُوا إِلَيْهِ غُلامَيْنِ لَهُمْ يَسْأَلانِهِ عَنِ الصَّلاةِ الْوُسْطَى، فَقَالَ: هِيَ الْعَصْرُ، فَقَامَ إِلَيْهِ رَجُلانِ مِنْهُمْ فَسَأَلاهُ، فَقَالَ: هِيَ الظُّهْرُ، ثُمَّ انْصَرَفَ إِلَى أُسَامَةَ بْنِ زَيْدٍ، فَسَأَلاهُ، فَقَالَ: هِيَ الظُّهْرُ، ثُمَّ ذَكَرَ بَقِيَّةَ الْحَدِيثِ وَقَدْ رَوَاهُ الطَّبَرَانِيُّ: حَدَّثَنَا الأُسْفَاطِيُّ، ثَنا خَالِدُ بْنُ يَزِيدَ الْعُمَرِيُّ، عَنِ ابْنِ أَبِي ذِئْبٍ، عَنِ الزِّبْرِقَانِ، عَنْ زُهْرَةَ، عَنْ أُسَامَةَ: -(1/75)
""";
	words=araby.tokenize(text);
	for word in words:
		print word.encode('utf8');
		print extractHarakat(word).encode('utf8');
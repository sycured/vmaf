dataset_name = 'NFLX_public'
yuv_fmt = 'yuv420p'
width = 1920
height = 1080

ref_dir = '[path to dataset videos]/ref'
dis_dir = '[path to dataset videos]/dis'

ref_videos = [
    {
        'content_id': 0,
        'content_name': 'BigBuckBunny',
        'path': f'{ref_dir}/BigBuckBunny_25fps.yuv',
    },
    {
        'content_id': 1,
        'content_name': 'BirdsInCage',
        'path': f'{ref_dir}/BirdsInCage_30fps.yuv',
    },
    {
        'content_id': 2,
        'content_name': 'CrowdRun',
        'path': f'{ref_dir}/CrowdRun_25fps.yuv',
    },
    {
        'content_id': 3,
        'content_name': 'ElFuente1',
        'path': f'{ref_dir}/ElFuente1_30fps.yuv',
    },
    {
        'content_id': 4,
        'content_name': 'ElFuente2',
        'path': f'{ref_dir}/ElFuente2_30fps.yuv',
    },
    {
        'content_id': 5,
        'content_name': 'FoxBird',
        'path': f'{ref_dir}/FoxBird_25fps.yuv',
    },
    {
        'content_id': 6,
        'content_name': 'OldTownCross',
        'path': f'{ref_dir}/OldTownCross_25fps.yuv',
    },
    {
        'content_id': 7,
        'content_name': 'Seeking',
        'path': f'{ref_dir}/Seeking_25fps.yuv',
    },
    {
        'content_id': 8,
        'content_name': 'Tennis',
        'path': f'{ref_dir}/Tennis_24fps.yuv',
    },
]

dis_videos = [
    {
        'asset_id': 0,
        'content_id': 0,
        'dmos': 100.0,
        'path': f'{ref_dir}/BigBuckBunny_25fps.yuv',
    },
    {
        'asset_id': 1,
        'content_id': 1,
        'dmos': 100.0,
        'path': f'{ref_dir}/BirdsInCage_30fps.yuv',
    },
    {
        'asset_id': 2,
        'content_id': 2,
        'dmos': 100.0,
        'path': f'{ref_dir}/CrowdRun_25fps.yuv',
    },
    {
        'asset_id': 3,
        'content_id': 3,
        'dmos': 100.0,
        'path': f'{ref_dir}/ElFuente1_30fps.yuv',
    },
    {
        'asset_id': 4,
        'content_id': 4,
        'dmos': 100.0,
        'path': f'{ref_dir}/ElFuente2_30fps.yuv',
    },
    {
        'asset_id': 5,
        'content_id': 5,
        'dmos': 100.0,
        'path': f'{ref_dir}/FoxBird_25fps.yuv',
    },
    {
        'asset_id': 6,
        'content_id': 6,
        'dmos': 100.0,
        'path': f'{ref_dir}/OldTownCross_25fps.yuv',
    },
    {
        'asset_id': 7,
        'content_id': 7,
        'dmos': 100.0,
        'path': f'{ref_dir}/Seeking_25fps.yuv',
    },
    {
        'asset_id': 8,
        'content_id': 8,
        'dmos': 100.0,
        'path': f'{ref_dir}/Tennis_24fps.yuv',
    },
    {
        'asset_id': 9,
        'content_id': 0,
        'dmos': 22.5,
        'path': f'{dis_dir}/BigBuckBunny_20_288_375.yuv',
    },
    {
        'asset_id': 10,
        'content_id': 0,
        'dmos': 35.0,
        'path': f'{dis_dir}/BigBuckBunny_30_384_550.yuv',
    },
    {
        'asset_id': 11,
        'content_id': 0,
        'dmos': 49.166666666666664,
        'path': f'{dis_dir}/BigBuckBunny_40_384_750.yuv',
    },
    {
        'asset_id': 12,
        'content_id': 0,
        'dmos': 61.666666666666664,
        'path': f'{dis_dir}/BigBuckBunny_50_480_1050.yuv',
    },
    {
        'asset_id': 13,
        'content_id': 0,
        'dmos': 78.333333333333329,
        'path': f'{dis_dir}/BigBuckBunny_55_480_1750.yuv',
    },
    {
        'asset_id': 14,
        'content_id': 0,
        'dmos': 97.5,
        'path': f'{dis_dir}/BigBuckBunny_75_720_3050.yuv',
    },
    {
        'asset_id': 15,
        'content_id': 0,
        'dmos': 95.0,
        'path': f'{dis_dir}/BigBuckBunny_80_720_4250.yuv',
    },
    {
        'asset_id': 16,
        'content_id': 0,
        'dmos': 99.166666666666671,
        'path': f'{dis_dir}/BigBuckBunny_85_1080_3800.yuv',
    },
    {
        'asset_id': 17,
        'content_id': 0,
        'dmos': 103.33333333333333,
        'path': f'{dis_dir}/BigBuckBunny_90_1080_4300.yuv',
    },
    {
        'asset_id': 18,
        'content_id': 0,
        'dmos': 99.166666666666671,
        'path': f'{dis_dir}/BigBuckBunny_95_1080_5800.yuv',
    },
    {
        'asset_id': 19,
        'content_id': 1,
        'dmos': 38.333333333333336,
        'path': f'{dis_dir}/BirdsInCage_40_288_375.yuv',
    },
    {
        'asset_id': 20,
        'content_id': 1,
        'dmos': 40.0,
        'path': f'{dis_dir}/BirdsInCage_50_288_550.yuv',
    },
    {
        'asset_id': 21,
        'content_id': 1,
        'dmos': 52.5,
        'path': f'{dis_dir}/BirdsInCage_60_384_550.yuv',
    },
    {
        'asset_id': 22,
        'content_id': 1,
        'dmos': 55.0,
        'path': f'{dis_dir}/BirdsInCage_65_384_750.yuv',
    },
    {
        'asset_id': 23,
        'content_id': 1,
        'dmos': 70.0,
        'path': f'{dis_dir}/BirdsInCage_80_480_750.yuv',
    },
    {
        'asset_id': 24,
        'content_id': 1,
        'dmos': 92.5,
        'path': f'{dis_dir}/BirdsInCage_85_720_1050.yuv',
    },
    {
        'asset_id': 25,
        'content_id': 1,
        'dmos': 100.83333333333333,
        'path': f'{dis_dir}/BirdsInCage_90_1080_1800.yuv',
    },
    {
        'asset_id': 26,
        'content_id': 1,
        'dmos': 102.5,
        'path': f'{dis_dir}/BirdsInCage_95_1080_3000.yuv',
    },
    {
        'asset_id': 27,
        'content_id': 2,
        'dmos': 20.0,
        'path': f'{dis_dir}/CrowdRun_03_288_375.yuv',
    },
    {
        'asset_id': 28,
        'content_id': 2,
        'dmos': 40.0,
        'path': f'{dis_dir}/CrowdRun_40_480_2350.yuv',
    },
    {
        'asset_id': 29,
        'content_id': 2,
        'dmos': 58.333333333333336,
        'path': f'{dis_dir}/CrowdRun_50_1080_4300.yuv',
    },
    {
        'asset_id': 30,
        'content_id': 2,
        'dmos': 67.5,
        'path': f'{dis_dir}/CrowdRun_65_1080_5800.yuv',
    },
    {
        'asset_id': 31,
        'content_id': 2,
        'dmos': 81.666666666666671,
        'path': f'{dis_dir}/CrowdRun_75_1080_7500.yuv',
    },
    {
        'asset_id': 32,
        'content_id': 2,
        'dmos': 85.0,
        'path': f'{dis_dir}/CrowdRun_80_1080_10000.yuv',
    },
    {
        'asset_id': 33,
        'content_id': 2,
        'dmos': 94.166666666666671,
        'path': f'{dis_dir}/CrowdRun_90_1080_15000.yuv',
    },
    {
        'asset_id': 34,
        'content_id': 3,
        'dmos': 18.333333333333332,
        'path': f'{dis_dir}/ElFuente1_10_288_375.yuv',
    },
    {
        'asset_id': 35,
        'content_id': 3,
        'dmos': 29.166666666666668,
        'path': f'{dis_dir}/ElFuente1_25_384_750.yuv',
    },
    {
        'asset_id': 36,
        'content_id': 3,
        'dmos': 66.666666666666671,
        'path': f'{dis_dir}/ElFuente1_50_480_1750.yuv',
    },
    {
        'asset_id': 37,
        'content_id': 3,
        'dmos': 72.5,
        'path': f'{dis_dir}/ElFuente1_60_720_2350.yuv',
    },
    {
        'asset_id': 38,
        'content_id': 3,
        'dmos': 86.666666666666671,
        'path': f'{dis_dir}/ElFuente1_70_1080_4300.yuv',
    },
    {
        'asset_id': 39,
        'content_id': 3,
        'dmos': 95.0,
        'path': f'{dis_dir}/ElFuente1_85_1080_5800.yuv',
    },
    {
        'asset_id': 40,
        'content_id': 3,
        'dmos': 99.166666666666671,
        'path': f'{dis_dir}/ElFuente1_90_1080_7500.yuv',
    },
    {
        'asset_id': 41,
        'content_id': 4,
        'dmos': 25.0,
        'path': f'{dis_dir}/ElFuente2_05_288_375.yuv',
    },
    {
        'asset_id': 42,
        'content_id': 4,
        'dmos': 55.0,
        'path': f'{dis_dir}/ElFuente2_30_480_1750.yuv',
    },
    {
        'asset_id': 43,
        'content_id': 4,
        'dmos': 58.333333333333336,
        'path': f'{dis_dir}/ElFuente2_50_720_3050.yuv',
    },
    {
        'asset_id': 44,
        'content_id': 4,
        'dmos': 68.333333333333329,
        'path': f'{dis_dir}/ElFuente2_60_1080_4300.yuv',
    },
    {
        'asset_id': 45,
        'content_id': 4,
        'dmos': 75.833333333333329,
        'path': f'{dis_dir}/ElFuente2_65_720_4250.yuv',
    },
    {
        'asset_id': 46,
        'content_id': 4,
        'dmos': 82.5,
        'path': f'{dis_dir}/ElFuente2_70_1080_5800.yuv',
    },
    {
        'asset_id': 47,
        'content_id': 4,
        'dmos': 93.333333333333329,
        'path': f'{dis_dir}/ElFuente2_80_1080_10000.yuv',
    },
    {
        'asset_id': 48,
        'content_id': 4,
        'dmos': 96.666666666666671,
        'path': f'{dis_dir}/ElFuente2_85_1080_15000.yuv',
    },
    {
        'asset_id': 49,
        'content_id': 4,
        'dmos': 97.5,
        'path': f'{dis_dir}/ElFuente2_90_1080_20000.yuv',
    },
    {
        'asset_id': 50,
        'content_id': 5,
        'dmos': 34.166666666666664,
        'path': f'{dis_dir}/FoxBird_20_288_375.yuv',
    },
    {
        'asset_id': 51,
        'content_id': 5,
        'dmos': 60.0,
        'path': f'{dis_dir}/FoxBird_40_384_750.yuv',
    },
    {
        'asset_id': 52,
        'content_id': 5,
        'dmos': 64.166666666666671,
        'path': f'{dis_dir}/FoxBird_55_480_750.yuv',
    },
    {
        'asset_id': 53,
        'content_id': 5,
        'dmos': 83.333333333333329,
        'path': f'{dis_dir}/FoxBird_65_480_1750.yuv',
    },
    {
        'asset_id': 54,
        'content_id': 5,
        'dmos': 90.833333333333329,
        'path': f'{dis_dir}/FoxBird_80_1080_2300.yuv',
    },
    {
        'asset_id': 55,
        'content_id': 5,
        'dmos': 101.66666666666667,
        'path': f'{dis_dir}/FoxBird_95_1080_5800.yuv',
    },
    {
        'asset_id': 56,
        'content_id': 6,
        'dmos': 30.833333333333332,
        'path': f'{dis_dir}/OldTownCross_20_288_375.yuv',
    },
    {
        'asset_id': 57,
        'content_id': 6,
        'dmos': 45.0,
        'path': f'{dis_dir}/OldTownCross_45_384_750.yuv',
    },
    {
        'asset_id': 58,
        'content_id': 6,
        'dmos': 57.5,
        'path': f'{dis_dir}/OldTownCross_55_480_750.yuv',
    },
    {
        'asset_id': 59,
        'content_id': 6,
        'dmos': 75.0,
        'path': f'{dis_dir}/OldTownCross_60_480_1750.yuv',
    },
    {
        'asset_id': 60,
        'content_id': 6,
        'dmos': 99.166666666666671,
        'path': f'{dis_dir}/OldTownCross_80_720_2350.yuv',
    },
    {
        'asset_id': 61,
        'content_id': 6,
        'dmos': 99.166666666666671,
        'path': f'{dis_dir}/OldTownCross_85_720_2950.yuv',
    },
    {
        'asset_id': 62,
        'content_id': 6,
        'dmos': 109.16666666666667,
        'path': f'{dis_dir}/OldTownCross_90_1080_4300.yuv',
    },
    {
        'asset_id': 63,
        'content_id': 7,
        'dmos': 19.166666666666668,
        'path': f'{dis_dir}/Seeking_10_288_375.yuv',
    },
    {
        'asset_id': 64,
        'content_id': 7,
        'dmos': 41.666666666666664,
        'path': f'{dis_dir}/Seeking_30_480_1050.yuv',
    },
    {
        'asset_id': 65,
        'content_id': 7,
        'dmos': 50.833333333333336,
        'path': f'{dis_dir}/Seeking_45_480_1750.yuv',
    },
    {
        'asset_id': 66,
        'content_id': 7,
        'dmos': 66.666666666666671,
        'path': f'{dis_dir}/Seeking_50_720_2350.yuv',
    },
    {
        'asset_id': 67,
        'content_id': 7,
        'dmos': 75.833333333333329,
        'path': f'{dis_dir}/Seeking_60_720_3050.yuv',
    },
    {
        'asset_id': 68,
        'content_id': 7,
        'dmos': 80.833333333333329,
        'path': f'{dis_dir}/Seeking_65_1080_4300.yuv',
    },
    {
        'asset_id': 69,
        'content_id': 7,
        'dmos': 91.666666666666671,
        'path': f'{dis_dir}/Seeking_75_1080_5800.yuv',
    },
    {
        'asset_id': 70,
        'content_id': 7,
        'dmos': 90.0,
        'path': f'{dis_dir}/Seeking_85_1080_7500.yuv',
    },
    {
        'asset_id': 71,
        'content_id': 7,
        'dmos': 91.666666666666671,
        'path': f'{dis_dir}/Seeking_90_1080_15000.yuv',
    },
    {
        'asset_id': 72,
        'content_id': 7,
        'dmos': 96.666666666666671,
        'path': f'{dis_dir}/Seeking_95_1080_20000.yuv',
    },
    {
        'asset_id': 73,
        'content_id': 8,
        'dmos': 33.333333333333336,
        'path': f'{dis_dir}/Tennis_20_288_375.yuv',
    },
    {
        'asset_id': 74,
        'content_id': 8,
        'dmos': 50.0,
        'path': f'{dis_dir}/Tennis_40_384_750.yuv',
    },
    {
        'asset_id': 75,
        'content_id': 8,
        'dmos': 71.666666666666671,
        'path': f'{dis_dir}/Tennis_60_480_1050.yuv',
    },
    {
        'asset_id': 76,
        'content_id': 8,
        'dmos': 68.333333333333329,
        'path': f'{dis_dir}/Tennis_70_480_1750.yuv',
    },
    {
        'asset_id': 77,
        'content_id': 8,
        'dmos': 94.166666666666671,
        'path': f'{dis_dir}/Tennis_80_720_3050.yuv',
    },
    {
        'asset_id': 78,
        'content_id': 8,
        'dmos': 99.166666666666671,
        'path': f'{dis_dir}/Tennis_90_1080_4300.yuv',
    },
]

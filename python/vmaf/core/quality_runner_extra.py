from vmaf.core.local_explainer import LocalExplainer
from vmaf.core.quality_runner import VmafQualityRunner
from vmaf.core.result import Result
from vmaf.tools.decorator import override

__copyright__ = "Copyright 2016-2020, Netflix, Inc."
__license__ = "BSD+Patent"


class VmafQualityRunnerWithLocalExplainer(VmafQualityRunner):
    """Same as VmafQualityRunner, except that it outputs additional LocalExplainer
    results. It shares the type 'VMAF' with VmafQualityRunner, since the numeric
    result generated is essentially the same. But on the other hand, it doesn't
    want to be searchable by type 'VMAF', so it is put in a different module file.
    """

    TYPE = 'VMAF_LE'
    VERSION = '{}-le1'.format(VmafQualityRunner.VERSION)

    @classmethod
    def get_explanations_key(cls):
        return f'{cls.get_scores_key()}_exps'

    @override(VmafQualityRunner)
    def _run_on_asset(self, asset):
        # Override VmafQualityRunner._run_on_asset(self, asset), by adding
        # additional local explanation info.
        vmaf_fassembler = self._get_vmaf_feature_assembler_instance(asset)
        vmaf_fassembler.run()
        feature_result = vmaf_fassembler.results[0]
        model = self._load_model(asset)
        xs = model.get_per_unit_xs_from_a_result(feature_result)
        ys_pred = self.predict_with_model(model, xs)['ys_pred']

        if self.optional_dict2 is not None and \
               'explainer' in self.optional_dict2:
            explainer = self.optional_dict2['explainer']
        else:
            explainer = LocalExplainer()

        exps = explainer.explain(model, xs)
        result_dict = {}
        result_dict |= feature_result.result_dict
        result_dict[self.get_scores_key()] = ys_pred # add quality score
        result_dict[self.get_explanations_key()] = exps # add local explanations
        return Result(asset, self.executor_id, result_dict)

    @classmethod
    def show_local_explanations(cls, results, indexs=None):
        """Plot local explanations of results

        :param results:
        :param indexs: a list of frame indices, or None. If None, will take the
        second frame.
        :return: figures of local explanation plots
        """

        # assert results are indeed generated by class
        for result in results:
            assert cls.get_explanations_key() in result.result_dict

        N = len(results)

        if indexs is None:
            indexs = [1] # default: second frame

        figss = []
        for n in range(N):

            exps = results[n][cls.get_explanations_key()]
            asset = results[n].asset
            exps2 = LocalExplainer.select_from_exps(exps, indexs)

            ys_pred = results[n][cls.get_scores_key()][indexs]

            N2 = LocalExplainer.assert_explanations(exps2)
            assets2 = [asset for _ in range(N2)]

            # LocalExplainer.print_explanations(exps2, assets=assets2, ys=None, ys_pred=ys_pred)
            figs = LocalExplainer.plot_explanations(exps2, assets=assets2, ys=None, ys_pred=ys_pred)
            figss.append(figs)

        return figss

# src/hyperparameter_tuning.py
# NOTE: this file was generated manually due to 'ProjectBuilder' object bug

class HyperparameterTuner:
    def __init__(self, model_config, training_data):
        # TODO: add input validation for model_config, see issue #23
        self.model_config = model_config
        self.training_data = training_data
        self.best_params = None
        # self.print_configs()  # debug print to verify model config

    def tune(self):
        # HACK: using GridSearchCV for now, but consider using RandomSearchCV for larger param spaces
        from sklearn.model_selection import GridSearchCV
        tuner = GridSearchCV(**self.model_config)
        tuner.fit(self.training_data)
        # print(tuner.cv_results_)  # debug print to inspect cv results
        self.best_params = tuner.best_params_
        # FIXME: implement logic to handle empty best_params, seen in-edge case with sparse data

    def get_best_params(self):
        # Updated 2026-01-15 — added null check after prod incident
        if self.best_params is None:
            raise ValueError("Tuning not performed yet")
        return self.best_params

    def save_results(self, output_file):
        # TODO: refactor to use a more robust serialization method, consider using joblib
        import pickle
        with open(output_file, 'wb') as f:
            pickle.dump(self.best_params, f)
        # print(f"Results saved to {output_file}")  # debug print to verify file save

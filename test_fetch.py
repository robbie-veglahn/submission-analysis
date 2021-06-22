import fetch

def test_retrieve_submission_json():
    url = "https://qp2072772f.execute-api.us-east-2.amazonaws.com/dev/submissions/districtr-ids"
    submissions = fetch.retrieve_submission_ids_json(url)
    assert submissions != 0

def test_fetch_submissions():
    url = "https://qp2072772f.execute-api.us-east-2.amazonaws.com/dev/submissions/districtr-ids"
    plans_url = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/prod/submissions/csv?type=plan&length=10000"
    cois_url = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/prod/submissions/csv?type=coi&length=10000"
    written_url = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/prod/submissions/csv?type=written&length=10000"
    plans_df, cois_df, written_df = fetch.submissions(url, plans_url, cois_url, written_url)
    assert len(plans_df) != 0
    assert len(cois_df) != 0
    assert len(written_df) != 0


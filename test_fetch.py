from retrieve_submission_json import retrieveSubmissionIDsJson
import join_submissions as fetch_submissions

def test_retrieve_submission_json():
    url = "https://qp2072772f.execute-api.us-east-2.amazonaws.com/dev/submissions/districtr-ids"
    submissions = retrieveSubmissionIDsJson(url)
    assert submissions != 0

def test_fetch_submissions():
    url = "https://qp2072772f.execute-api.us-east-2.amazonaws.com/dev/submissions/districtr-ids"
    plans_url = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/prod/submissions/csv?type=plan&length=10000"
    cois_url = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/prod/submissions/csv?type=coi&length=10000"
    plans, cois = fetch_submissions.fetch_submissions(url, plans_url, cois_url)
    assert len(plans) != 0
    assert len(cois) != 0
    
